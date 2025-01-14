import os
from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()

# Define the function to fetch a response from the Groq API
def get_groq_response(prompt, model="llama-3.3-70b-versatile"):
    """
    Function to get a response from the Groq API.
    
    Args:
        prompt (str): The user's input or question.
        model (str): The language model to use (default is "llama-3.3-70b-versatile").
    
    Returns:
        str: The assistant's response.
    """
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Behave like a Medical Professional Doctor"},
            {"role": "user", "content": prompt},
        ],
        model=model,
    )
    
    return chat_completion.choices[0].message.content


# Example usage
if __name__ == "__main__":
    user_prompt = "I am a 21 years old and having a fever of 99 degree"
    
    prompt = f'''
    {user_prompt}
    return in the json format like 
    {{
        description: message from the doctor
        medicines: presescribed medicines seperated by comma
    }}
    '''
    response = get_groq_response(prompt)
    print(response)

