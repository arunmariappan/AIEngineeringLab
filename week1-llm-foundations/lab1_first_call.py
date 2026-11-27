"""Lab 1: Your first LLM call.

Part 1 - run the same prompt three times and watch the answer change.
Part 2 - turn the one knob you do get on this model, `effort`, on a question
         (a tea-stall bill), and watch thinking tokens, seconds and the answer.
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
    # CHANGE ME (Lab 1, step 4): swap this prompt for one from your job, e.g.
    #   "Summarise this alert in one line: disk usage on db-01 is 91% and rising."
    tagline = "Give me a one-sentence tagline for a coffee shop that only sells cold brew."

    print("### Part 1 - same prompt, three runs. Are they all the same?\n")
    for run in range(1, 4):
        answer, _, _ = ask(tagline)
        print(f"--- run {run} ---\n{answer}\n")

    print("### Part 2 - same question, three effort levels. Watch thinking tokens and seconds.\n")
    question = (
        "At a tea stall, tea costs Rs 15 and coffee costs Rs 25. A group bought 13 drinks "
        "and paid Rs 245. How many coffees did they buy? Answer in one line."
    )
    for effort in ("low", "medium", "high"):
        answer, message, seconds = ask(question, effort=effort)
        details = message.usage.output_tokens_details
        thinking = details.thinking_tokens if details else 0
        print(f"--- effort={effort}: {message.usage.output_tokens} output tokens "
              f"(thinking {thinking}), {seconds:.1f}s, stop_reason={message.stop_reason} ---")
        print(f"{answer}\n")

    # EXTEND (Lab 1, steps 6-7):
    #   a) add  temperature=0,  as a new line inside the create() call above, run, and read the error.
    #   b) set  max_tokens=20  and run again: stop_reason turns into "max_tokens". Put 1024 back after.
    # About (a):
    #   You'll get a TypeError before any request is sent: the current SDK doesn't
    #   even have the parameter, and Haiku 5.5's docs say to leave sampling settings
    #   out. You cannot opt out of variance - which is exactly why, from Week 2,
    #   we MEASURE outputs instead of asserting them.
