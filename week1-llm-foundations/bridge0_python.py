"""Bridge 0: read Python before Saturday. No API key needed; nothing leaves your laptop.

Run it:    uv run bridge0_python.py
Then read it from top to bottom. The numbered comments (1 to 8) match the eight boxes on
Saturday's slide "Read Python in ten minutes" and on the Bridge 0 page. They're numbered
the way the slide teaches them, so in this file they don't appear in order.

fake_reply() pretends to be the AI service. It sends back a reply shaped exactly like the
real one: a dictionary holding a LIST of blocks, plus a usage "receipt".
"""
# 1 · IMPORT: bring in a toolbox someone else wrote. These two come with Python.
import json
import random

# 2 · VARIABLE: a labelled box that holds a value. CAPITALS mean "set once, don't change".
MODEL = "pretend-model"            # Saturday's labs use "claude-haiku-5-5"


# 3 · FUNCTION: a named recipe. `effort` has a default, so you may leave it out.
def fake_reply(prompt, effort="low"):
    """Return a reply shaped like the real API's."""
    # 6 · LIST and DICT: a list keeps things in order; a dict maps label -> value.
    taglines = [
        "Cold brew. Warm welcome.",
        "Slow-steeped. Wide awake.",
        "Chilled, never rushed.",
    ]
    thinking_tokens = {"low": 5, "medium": 40, "high": 120}
    answer = random.choice(taglines)          # random, like a real model: run it twice and compare
    return {
        "model": MODEL,
        "content": [
            {"type": "thinking", "thinking": "They want something short and upbeat..."},
            {"type": "text", "text": answer},
        ],
        "usage": {
            "input_tokens": len(prompt) // 4,                              # about 4 characters per token
            "output_tokens": thinking_tokens[effort] + len(answer) // 4,   # thinking counts as output
        },
    }


def text_of(reply):
    """Pick the text blocks by their type, never by position: the first block may be thinking."""
    return "".join(block["text"] for block in reply["content"] if block["type"] == "text")


if __name__ == "__main__":
    # CHANGE ME (Bridge 0, step 4): write your own prompt here, then run the file again.
    prompt = "Give me a one-sentence tagline for a coffee shop that only sells cold brew."

    # 5 · LOOP: do the indented lines 3 times. range(1, 4) gives 1, 2, 3 (it stops BEFORE 4).
    for run in range(1, 4):
        reply = fake_reply(prompt)                    # 4 · CALLING IT: use the recipe
        print(f"run {run}: {text_of(reply)}")         # 7 · F-STRING: text with the blanks filled in

    # 4 · CALLING IT again, changing one setting by name.
    reply = fake_reply(prompt, effort="high")
    print(f"\neffort=high: {reply['usage']['output_tokens']} output tokens")

    # The whole reply, printed as JSON: the shape every AI API sends back.
    print("\nThe full reply, as JSON:")
    print(json.dumps(reply, indent=2))

# 8 · COMMENT: everything after a # is a note for humans. Python skips it.
