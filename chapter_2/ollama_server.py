from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:11434/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="gemma3:1b", # this field is needed for ollama server
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)