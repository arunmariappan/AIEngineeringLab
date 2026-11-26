# Lesson 12 of 12 - reading a file, and JSON
#     uv run python_basics/12_files_and_json.py
# Run it from the week1-llm-foundations folder: the paths below start from there.

import json
from pathlib import Path

text = Path("python_basics/alert.txt").read_text(encoding="utf-8")   # the whole file, as one string
print(text)
lines = text.splitlines()                 # one string per line
print(len(lines), "lines; the first is:", lines[0])

raw = Path("python_basics/ticket.json").read_text(encoding="utf-8")
ticket = json.loads(raw)                  # JSON text -> a Python dict
print(type(ticket))
print(ticket["priority"], "-", ticket["summary"])
print(ticket["tags"][0])

ticket["status"] = "triaged"
print(json.dumps(ticket, indent=2))       # a Python dict -> JSON text again

# Lab 3 loads its prompt the same way: Path("prompts/extract_ticket.md").read_text(...)

# CHANGE ME: change "priority" in python_basics/ticket.json to "urgent", save it, and run again.
