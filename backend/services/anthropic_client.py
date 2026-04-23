import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

_client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

SYSTEM_PROMPT = (
    "You are an expert on Intent-Driven Engineering — a discipline that uses "
    "structured intent files to drive AI-assisted software development. "
    "Answer clearly and concisely for enterprise engineers."
)


def chat(message: str) -> dict:
    response = _client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": message}],
    )
    return {
        "text": response.content[0].text,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    }
