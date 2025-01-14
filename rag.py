from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import pinecone
from chat_module import GroqLLM
from langchain import PromptTemplate

class ChatBot():
    load_dotenv()

    # Use PyPDFLoader to load a PDF file
    loader = PyPDFLoader('./jess101.pdf')
    documents = loader.load()

    # Split the document into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=4)
    docs = text_splitter.split_documents(documents)

    # Generate embeddings
    embeddings = HuggingFaceEmbeddings()


    # Initialize Pinecone client
    pinecone.init(
        api_key= os.getenv('PINECORN_API_KEY'),
        environment='gcp-starter'
    )

    # Define Index Name
    index_name = "MED_BOT"

    # Checking Index
    if index_name not in pinecone.list_indexes():
      # Create new Index
      pinecone.create_index(name=index_name, metric="cosine", dimension=768)
      docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    else:
      # Link to the existing index
      docsearch = Pinecone.from_existing_index(index_name, embeddings)
  
  
    # Instantiate the custom LLM
    llm = GroqLLM()

    template = """
    You are a fortune teller. These Human will ask you a questions about their life. 
    Use following piece of context to answer the question. 
    If you don't know the answer, just say you don't know. 
    Keep the answer within 2 sentences and concise.

    Context: {context}
    Question: {question}
    Answer: 

    """

    prompt = PromptTemplate(
      template=template, 
      input_variables=["context", "question"]
    )


    rag_chain = (
      {"context": docsearch.as_retriever(),  "question": RunnablePassthrough()} 
      | prompt 
      | llm
      | StrOutputParser() 
    )
