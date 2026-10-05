"""Step 4: compare outputs across temperatures.
Runs the same prompt several times per temperature so you can see variance."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
MODEL = os.getenv("MODEL", "gpt-4o-mini")

PROMPT = "Write a one-line startup idea for students in India."
TEMPERATURES = [0.0, 0.7, 1.2, 1.8]
RUNS = 3

for t in TEMPERATURES:
    print(f"\n{'=' * 60}\ntemperature = {t}\n{'=' * 60}")
    outputs = []
    for i in range(RUNS):
        r = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": PROMPT}],
            temperature=t,
            max_tokens=60,
        )
        text = r.choices[0].message.content.strip()
        outputs.append(text)
        print(f"  run {i + 1}: {text}")
    print(f"  -> unique outputs: {len(set(outputs))}/{RUNS}")

# Expect: temp 0 = (nearly) identical every run, higher = more varied,
# and ~1.8+ can get weird or incoherent.
