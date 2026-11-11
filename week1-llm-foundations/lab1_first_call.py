"""Lab 1: Your first LLM call.

Part 1 - run the same prompt three times and watch the answer change.
Part 2 - turn the one knob you do get on this model, `effort`, and watch
         tokens, seconds and the answer change with it.
"""
import time

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()          # reads ANTHROPIC_API_KEY (+ optional ANTHROPIC_BASE_URL) from .env
client = Anthropic()   # picks the key up from the environment

MODEL = "claude-haiku-5-5"


def text_of(message) -> str:
    """A response is a LIST of content blocks, not a string.

    Haiku 5.5 thinks by default, so the first block can be a `thinking`
    block. Pick the text blocks by their type, never by position.
    """
    return "".join(block.text for block in message.content if block.type == "text")


def ask(prompt: str, effort: str = "low"):
    started = time.perf_counter()
    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,                     # a CEILING for thinking + answer together, not a target
        output_config={"effort": effort},    # low | medium | high | xhigh | max
        messages=[{"role": "user", "content": prompt}],
    )
    seconds = time.perf_counter() - started
    return text_of(message), message, seconds


if __name__ == "__main__":
    tagline = "Give me a one-sentence tagline for a coffee shop that only sells cold brew."

    print("### Part 1 - same prompt, three runs. Expect three different answers.\n")
    for run in range(1, 4):
        answer, _, _ = ask(tagline)
        print(f"--- run {run} ---\n{answer}\n")

    print("### Part 2 - same question, three effort levels. Watch tokens and seconds.\n")
    question = (
        "A train leaves at 09:40 and arrives at 13:15. It stops for 25 minutes "
        "on the way. How long was it actually moving? Answer in one line."
    )
    for effort in ("low", "medium", "high"):
        answer, message, seconds = ask(question, effort=effort)
        print(f"--- effort={effort}: {message.usage.output_tokens} output tokens, {seconds:.1f}s ---")
        print(f"{answer}\n")

    # STRETCH (try it, then read the error):
    #   add  temperature=0  to the create() call above.
    #   You'll get a TypeError before any request is sent: the current SDK doesn't
    #   even have the parameter, and Haiku 5.5's docs say to leave sampling settings
    #   out. You cannot opt out of variance - which is exactly why, from Week 2,
    #   we MEASURE outputs instead of asserting them.
