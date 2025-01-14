from rag import ChatBot
# Outside ChatBot() class
bot = ChatBot()
input = "what are the types of Resources on the basis of origin"
result = bot.rag_chain.invoke(input)
print(result)
