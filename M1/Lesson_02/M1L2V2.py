# import packages
from dotenv import load_dotenv
import openai

# load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Explain generative AI in one sentence."}
    ],
    temperature=0.7,
    max_tokens=100
)

# print the response from OpenAI
print(response.choices[0].message.content)
