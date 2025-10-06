import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE")
model = os.getenv("MODEL")

# Ensure the API key is available
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")
client = OpenAI(api_key=api_key, base_url=base_url)


# Example function to query ChatGPT
def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model=model,  # gpt-4 turbo or a model of your preference
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_message}],
        temperature=0.7,
    )
    return response.choices[0].message.content


# Example usage
user = "What is the capital of France?"
response = ask_chatgpt(user)
print(response)
