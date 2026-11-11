"""Stretch: Haiku 5.5 vs Sonnet 5.5 on the same question.

Sonnet 5.5 costs 20x as much per token. Is the answer 20x better?
Today you eyeball it. From Week 2 you'll score it.
"""
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

# USD per million tokens (standard tier; verify at platform.claude.com/docs/en/about-claude/pricing, Nov 2026)
MODELS = {
    "claude-haiku-5-5":  {"input": 0.10, "output": 0.50},
    "claude-sonnet-5-5": {"input": 2.00, "output": 10.00},
}

QUESTION = (
    "Our nightly deploy failed with 'connection refused' to the database, but only "
    "in staging. List the three most likely causes, most likely first, one line each."
)


def text_of(message) -> str:
    return "".join(block.text for block in message.content if block.type == "text")


if __name__ == "__main__":
    for model, rate in MODELS.items():
        message = client.messages.create(
            model=model,
            max_tokens=1024,
            output_config={"effort": "low"},
            messages=[{"role": "user", "content": QUESTION}],
        )
        u = message.usage
        cost = u.input_tokens / 1e6 * rate["input"] + u.output_tokens / 1e6 * rate["output"]
        print(f"=== {model}  ({u.input_tokens} in / {u.output_tokens} out = ${cost:.5f}) ===")
        print(text_of(message), "\n")
