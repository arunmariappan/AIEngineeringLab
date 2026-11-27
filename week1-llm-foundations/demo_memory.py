"""Demo: the model remembers nothing between calls (slide 24, about 60 seconds).

Call 1 tells it a name. Call 2 asks for the name WITHOUT sending call 1.
Call 3 asks again, this time sending the whole conversation so far.
Chat apps do call 3 on every message: that is all their "memory" is.

Run it:  uv run demo_memory.py
"""
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

MODEL = "claude-haiku-5-5"
QUESTION = "What's my name, and what do I look after?"


def text_of(message) -> str:
    """Pick text blocks by type - the first block may be a `thinking` block."""
    return "".join(block.text for block in message.content if block.type == "text")


def ask(messages: list) -> str:
    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        output_config={"effort": "low"},
        messages=messages,
    )
    return text_of(message)


if __name__ == "__main__":
    # CHANGE ME: put your own name and job in this first message.
    first = [{"role": "user", "content": "Hi! I'm Priya, and I look after the payments service."}]

    reply = ask(first)
    print("Call 1 - you introduce yourself:")
    print(f"  {reply}\n")

    print("Call 2 - a brand-new call, sent WITHOUT call 1:")
    print(f"  {ask([{'role': 'user', 'content': QUESTION}])}\n")

    history = first + [
        {"role": "assistant", "content": reply},     # what it said in call 1
        {"role": "user", "content": QUESTION},       # the new question
    ]
    print("Call 3 - the same question, but this time we send the conversation too:")
    print(f"  {ask(history)}\n")

    print("The model is stateless. 'Memory' is your code sending the conversation again, on every call.")
