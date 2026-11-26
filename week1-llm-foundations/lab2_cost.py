"""Lab 2: Every call has a price. Read the receipt (`usage`), compute the cost,
scale it up, and find the 100K cliff.

Each run also saves its receipt to results/week1_cost.txt (checkpoint item 1:
run it with YOUR question, then commit that file)."""
from datetime import datetime
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

MODEL = "claude-haiku-5-5"

# CHANGE ME (Lab 2, step 4): replace this question with one from your own job.
QUESTION = "Summarise the CAP theorem for a backend engineer in 3 bullet points."
# CHANGE ME (Lab 2, step 5): try "medium", then "high". Put "low" back afterwards.
EFFORT = "low"

RESULTS_FILE = Path("results/week1_cost.txt")

# Claude Haiku 5.5 list prices, USD per MILLION tokens.
# Verify before quoting: platform.claude.com/docs/en/about-claude/pricing (checked Nov 2026).
# The rate depends on how long the PROMPT is: past 100,000 input tokens, every rate is 5x.
PRICES = {
    "standard": {"input": 0.10, "output": 0.50},   # prompt up to 100K tokens
    "long":     {"input": 0.50, "output": 2.50},   # prompt over 100K tokens
}
LONG_PROMPT_THRESHOLD = 100_000


def text_of(message) -> str:
    """Pick text blocks by type - the first block may be a `thinking` block."""
    return "".join(block.text for block in message.content if block.type == "text")


def cost_usd(input_tokens: int, output_tokens: int) -> float:
    """Dollar cost of one call. (Prompt length counts ALL input tokens - with
    prompt caching that includes cache reads and writes, which we don't use today.)"""
    tier = "long" if input_tokens > LONG_PROMPT_THRESHOLD else "standard"
    rate = PRICES[tier]
    return (input_tokens / 1_000_000) * rate["input"] + (output_tokens / 1_000_000) * rate["output"]


if __name__ == "__main__":
    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        output_config={"effort": EFFORT},
        messages=[{"role": "user", "content": QUESTION}],
    )
    usage = message.usage   # the receipt - never guess token counts
    thinking = usage.output_tokens_details.thinking_tokens if usage.output_tokens_details else 0
    this_call = cost_usd(usage.input_tokens, usage.output_tokens)

    # Scale it up - the number finance actually asks for.
    calls_per_month = 10_000 * 5 * 30   # 10,000 questions/day x 5 calls each x 30 days

    receipt = [
        f"question       : {QUESTION}",
        f"model, effort  : {MODEL}, {EFFORT}",
        f"input tokens   : {usage.input_tokens}",
        f"output tokens  : {usage.output_tokens}   (output costs 5x input)",
        f"  of which thinking: {thinking}   (you pay for thinking too)",
        f"cost this call : ${this_call:.6f}",
        f"10,000 questions/day x 5 calls x 30 days: ${this_call * calls_per_month:,.2f} per month",
        "",
        # The cliff: same answer length, prompts just under and just over 100K tokens.
        "The 100K cliff (same output, bigger prompt):",
    ]
    for prompt_tokens in (99_000, 101_000):
        receipt.append(f"  prompt {prompt_tokens:>7,} tokens -> ${cost_usd(prompt_tokens, usage.output_tokens):.4f} per call")

    print(text_of(message))
    print("-" * 60)
    print("\n".join(receipt))

    # Save the receipt (checkpoint item 1). Each run replaces the file: your last run is the one kept.
    RESULTS_FILE.parent.mkdir(exist_ok=True)
    RESULTS_FILE.write_text(
        f"Week 1 cost receipt - {datetime.now():%Y-%m-%d %H:%M}\n\n"
        + "\n".join(receipt) + "\n\nAnswer:\n" + text_of(message) + "\n",
        encoding="utf-8",
    )
    print(f"\nReceipt saved to {RESULTS_FILE.as_posix()}")

    # EXTEND:
    #   1. Check "cost this call" by hand with the formula in cost_usd().
    #   2. At what prompt size does pasting "the whole wiki" stop being a rounding error?
