from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()  # loading and setting the api key can be done in one step

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE")
model = os.getenv("MODEL")

client = OpenAI(api_key=api_key,
        base_url=base_url)

# Example function to query ChatGPT
def ask_chatgpt(messages):
    response = client.chat.completions.create(       
        model=model,
        messages=messages,
        temperature=0.7,   
        response_format={"type": "json_object"},     
        )       
    
    return response.choices[0].message.content


messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant and always output JSON."  
        },
    {
        "role": "user",
        "content": "What is the captial of France?"
        },
    {
        "role": "assistant",
        "content": "The capital of France is Paris."
        },
    {
        "role": "user",
        "content": "What is an interesting fact of Paris."
        }
    ]
response = ask_chatgpt(messages)
print(response)
