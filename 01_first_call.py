"""Step 1: first API call. OpenAI() reads OPENAI_API_KEY from the environment."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # loads .env into environment variables
client = OpenAI()

MODEL = os.getenv("MODEL", "gpt-4o-mini")  # set MODEL in .env to switch providers

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Explain what a token is in one sentence."}],
)

print(response.choices[0].message.content)
print("\n--- usage ---")
print("prompt tokens:    ", response.usage.prompt_tokens)
print("completion tokens:", response.usage.completion_tokens)
print("total tokens:     ", response.usage.total_tokens)
print("finish_reason:    ", response.choices[0].finish_reason)
