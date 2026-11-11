# Spec: triage CLI  (write this BEFORE you ask the AI to build anything)

## What it does
<!-- One sentence. e.g. "Reads a support ticket and prints its priority, category and summary." -->

## Input
<!-- e.g. ticket text as a command-line argument, or piped on stdin -->

## Output
<!-- e.g. the three lines from prompts/extract_ticket.md, nothing else -->

## Acceptance checks (you will run these yourself)
1. <!-- e.g. `python triage.py "Export button throws 500 for all paid users"` prints priority: high or urgent -->
2. <!-- e.g. an empty ticket prints "unknown" for every field and does not crash -->

## Constraints
- Loads the prompt from prompts/extract_ticket.md (no inline prompt string)
- Reads the API key from the environment (never hard-coded)
- Uses claude-haiku-5-5
