# Lesson 7 of 12 - dicts: values with labels, and data inside data
#     uv run python_basics/07_dicts.py

usage = {"input_tokens": 31, "output_tokens": 52}    # label: value, label: value
print(usage["input_tokens"])          # look a value up by its label (its "key")

usage["thinking_tokens"] = 12         # add a new label and value
print(usage)
print(usage.get("cache_tokens", 0))   # .get() gives a default when the label is missing
print(len(usage))                     # how many labels

# Data inside data: a list of dicts inside a dict. This is the shape of an API reply.
reply = {
    "content": [
        {"type": "thinking", "thinking": "They want something short..."},
        {"type": "text", "text": "Cold brew. Warm welcome."},
    ],
    "usage": {"input_tokens": 31, "output_tokens": 52},
}
print(reply["usage"]["output_tokens"])   # step in one level at a time
print(reply["content"][1]["text"])       # the answer - but only because we KNOW it's second
print(reply["content"][0]["type"])       # the first block is thinking, not the answer

# CHANGE ME: add your own label to `usage`, e.g. usage["calls"] = 3, and print the whole dict.
