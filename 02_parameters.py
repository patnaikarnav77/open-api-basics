"""Step 2: experiment with system message, max_tokens, temperature."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
MODEL = os.getenv("MODEL", "gpt-4o-mini")
# gpt-oss models "think" before answering; keep that short so max_tokens isn't eaten
EXTRA = {"reasoning_effort": "low"} if "gpt-oss" in MODEL else {}


def ask(prompt, system="You are a helpful assistant.", **kwargs):
    r = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        **EXTRA,
        **kwargs,
    )
    return r.choices[0].message.content, r.choices[0].finish_reason


prompt = "Explain how the internet works."

print("=== 1. System message changes behavior ===")
for system in [
    "You are a pirate. Answer in pirate speak.",
    "You are a senior engineer. Be concise and technical.",
    "Explain everything like I'm 5.",
]:
    out, _ = ask(prompt, system=system, max_tokens=300)
    print(f"\n[{system}]\n{out}")

print("\n=== 2. max_tokens truncates output ===")
for n in [10, 50, 200]:
    out, reason = ask(prompt, max_tokens=n)
    print(f"\n[max_tokens={n} | finish_reason={reason}]\n{out}")
# finish_reason == "length" means the model got cut off

print("\n=== 3. temperature ===")
for t in [0, 1, 1.8]:
    out, _ = ask("Give me a name for a coffee shop.", temperature=t, max_tokens=300)
    print(f"[temperature={t}] {out}")
