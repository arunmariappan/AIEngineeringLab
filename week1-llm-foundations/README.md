# Week 1 — LLM Foundations

Model: `claude-haiku-5-5` · Session 1 · Saturday 14 November 2026

## Setup (5 minutes)
1. Copy `.env.example` to `.env` (`copy .env.example .env` on Windows, `cp .env.example .env` on macOS) and paste your class key.
2. `uv run lab1_first_call.py`. The first run creates `.venv` and installs everything from `pyproject.toml`.
   No uv? `python -m venv .venv`, activate it, `pip install -r requirements.txt`, then `python lab1_first_call.py`.
3. Claude Code on the class key: run `.\claude-class.cmd` (Windows) or `bash claude-class.sh` (macOS/Linux) from this folder. It uses your `.env` key and Haiku 5.5, and leaves your own Claude Code setup alone. Say **yes** when it asks to use the API key.

## Today's labs, in order
| When | File | What you'll see |
|---|---|---|
| 10:23 | `lab1_first_call.py` | Same prompt, three different answers — and the `effort` knob |
| ~10:50 | `tokens_minilab.py` | The same sentence in English, Hindi, Kannada and Tamil — counted |
| 11:08 | `lab2_cost.py` | The receipt (`usage`), cost per call, cost per month, the 100K cliff |
| 11:48 | `lab3_prompt_as_spec.py` | Your prompt as a versioned file you can `git diff` |
| 12:13 | `specs/triage_cli.md` | Write the spec first, then let your AI coding tool build it |
| stretch | `stretch_compare_models.py` | Haiku 5.5 vs Sonnet 5.5 — is 20× the price 20× better? |

## Two things that will trip you up
- **A response is a list of blocks.** Haiku 5.5 thinks by default, so the first block may be `thinking`. Every lab picks text blocks by `type`.
- **`max_tokens` covers thinking + answer.** Set it too low and you can get thinking with no answer.

## Step-by-step pages
Open `exercises/index.html` in your browser: the morning's run-sheet, one page per lab, and the Week 1 checkpoint.

## Homework (due before Week 2)
The four checkpoint items, and how to hand them in through your own private GitHub repo, are on `exercises/index.html`. Tag your work `git tag wk1-checkpoint`.
