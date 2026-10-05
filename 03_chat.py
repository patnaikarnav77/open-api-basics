"""Step 3: small interactive script. Type a message, get a reply. 'quit' to exit.
Keeps conversation history so the model remembers earlier turns."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
MODEL = os.getenv("MODEL", "gpt-4o-mini")

SYSTEM = "You are a friendly, concise assistant."
TEMPERATURE = 0.7
MAX_TOKENS = 300

messages = [{"role": "system", "content": SYSTEM}]

print("Chat started. Type 'quit' to exit.\n")
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"quit", "exit", "q"}:
        break
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})
    try:
        r = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )
    except Exception as e:
        print(f"[error] {e}")
        messages.pop()
        continue

    reply = r.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"AI: {reply}")
    print(f"    (tokens used: {r.usage.total_tokens})\n")
