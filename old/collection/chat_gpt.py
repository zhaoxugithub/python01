import openai
import json

openai.api_key = "YOUR_API_KEY_HERE"

model_engine = "text-davinci-002"
prompt = "Hello, I'm ChatGPT. How can I help you today?"

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.7
)

print(response.choices[0].text)
