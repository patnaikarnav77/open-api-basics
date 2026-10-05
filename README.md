# OpenAI API Basics
   Project: https://roadmap.sh/projects/openai-api-python
Calling LLMs directly from Python using the `openai` library: system messages, `temperature`, `max_tokens`, and a small interactive chat script.

Works with OpenAI or any OpenAI-compatible provider (e.g. Groq's free tier) by changing `.env` only.

## Setup

1. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   venv\Scripts\activate          # Mac/Linux: source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Copy `env.example` (or `.env.example`) to `.env` and fill it in.

   **OpenAI (paid):**
   ```
   OPENAI_API_KEY=sk-...
   MODEL=gpt-4o-mini
   ```
   **Groq (free tier):**
   ```
   OPENAI_API_KEY=gsk_...
   OPENAI_BASE_URL=https://api.groq.com/openai/v1
   MODEL=llama-3.3-70b-versatile
   ```
3. Never commit `.env`. It is listed in `.gitignore`.

## Scripts

| File | What it does |
|------|--------------|
| `01_first_call.py` | First `client.chat.completions.create()` call, prints token usage |
| `02_parameters.py` | Compares system messages, `max_tokens` values, and temperatures |
| `03_chat.py` | Interactive chat loop with conversation history |
| `04_temperature_compare.py` | Same prompt at several temperatures, multiple runs each |

## Results

Model: `openai/gpt-oss-20b` via Groq (OpenAI-compatible endpoint), `reasoning_effort="low"`.
Prompt: "Write a one-line startup idea for students in India." Each temperature run 3 times.

| Temperature | Unique outputs (of 3) | Observation |
|-------------|-----------------------|-------------|
| 0.0 | 1/3 | Identical text every run (deterministic) |
| 0.7 | 3/3 | Different ideas each time (marketplace, micro-learning) |
| 1.2 | 3/3 | More variety in structure and features |
| 1.8 | 3/3 | Most varied, but still coherent |

Sample at temperature 0 (all 3 runs identical):
> A mobile-first platform that connects Indian students with local mentors and micro-learning modules...

Coffee-shop name test (single run each):
- temp 0: short, bare name
- temp 1: name plus one-line explanation
- temp 1.8: name plus bullet-point reasoning (longer, more elaborate)

## What I learned

- Temperature controls randomness: 0 gives the same answer every run, higher values give varied answers. Higher temperature also changed response style and length, not just wording.
- Tokens are the unit of billing and limits. `response.usage` shows prompt, completion and total counts.
- `max_tokens` caps the reply; `finish_reason == "length"` means it was cut off.
- Reasoning models (like gpt-oss) use hidden "thinking" tokens that count toward `max_tokens`. With a small limit the visible reply came back empty. Fixed with `reasoning_effort="low"` and a higher limit.
- Because the OpenAI SDK reads `OPENAI_BASE_URL`, the same code works with OpenAI or Groq by editing `.env` only..
