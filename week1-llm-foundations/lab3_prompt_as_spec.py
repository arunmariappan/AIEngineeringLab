"""Lab 3: The prompt is source code. Keep it in the repo, load it, version it."""
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

MODEL = "claude-haiku-5-5"
PROMPT_FILE = Path("prompts/extract_ticket.md")


def text_of(message) -> str:
    """Pick text blocks by type - the first block may be a `thinking` block."""
    return "".join(block.text for block in message.content if block.type == "text")


def load_prompt(**values: str) -> str:
    """Load a versioned prompt file, drop '#' metadata lines, fill {placeholders}.

    Uses explicit replacement (not str.format) so JSON braces in a prompt never collide.
    """
    lines = PROMPT_FILE.read_text(encoding="utf-8").splitlines()
    body = "\n".join(line for line in lines if not line.startswith("#"))
    for key, value in values.items():
        body = body.replace("{" + key + "}", value)
    return body


def triage(ticket: str) -> str:
    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        output_config={"effort": "low"},
        messages=[{"role": "user", "content": load_prompt(ticket=ticket)}],
    )
    return text_of(message)


if __name__ == "__main__":
    ticket = (
        "Hi - since last night's deploy the Export button on the reports page "
        "throws a 500 for every user on our paid plan. It's blocking month-end "
        "reporting for finance. Please help ASAP."
    )
    print(triage(ticket))
    # Now: edit prompts/extract_ticket.md, re-run, and `git diff prompts/`.
    # The prompt change shows up as a reviewable diff - because it's source code.
