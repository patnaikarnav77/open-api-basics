# OpenAI API Basics

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

_Paste the output of `04_temperature_compare.py` here, then add notes._

## What I learned

- Tokens are the unit models read and bill by (~4 English characters each). `response.usage` shows counts.
- `temperature` controls randomness: 0 is near-deterministic, higher values give more varied (and eventually chaotic) output.
- `max_tokens` caps the reply. `finish_reason == "length"` means it got cut off.
- The system message sets the model's behavior and tone.
- Reasoning models (o-series, gpt-5 family) don't accept `temperature` and use `max_completion_tokens` instead of `max_tokens`.
