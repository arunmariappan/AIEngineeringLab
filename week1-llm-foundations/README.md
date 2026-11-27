# Week 1 — LLM Foundations

Model: `claude-haiku-5-5` · Session 1 · Saturday 28 November 2026, 10:00–13:00

## Before Saturday
1. **Set up your laptop:** follow `exercises/setup.html`, every step except step 10 (that one needs your key).
2. **Bridge 0, the basics:** `exercises/bridge0.html`. It covers the terminal, reading Python, error messages, git and `.env`, using `bridge0_python.py`, which needs no key.
3. **Never programmed before?** Then `exercises/python-basics.html`, *Python from zero*: twelve short lessons, one small file each in `python_basics/`. No key needed. Lessons 1–7 before Saturday if you can; the rest before Week 2.
4. Already cloned the repo at the intro? Get the latest files first: `git pull`.

Copy `.env.example` to `.env` (`copy .env.example .env` on Windows, `cp .env.example .env` on macOS). Your own class key arrives in a **private WhatsApp message at 09:30 on Saturday**: paste it into `.env`, then delete the message. Never commit it or post it in a chat.

## Saturday's labs, in order
Every lab runs the same way: **run it → read it → change it → extend it**. The lines to change are marked `# CHANGE ME`.

| When | File | What you'll see |
|---|---|---|
| 10:40 | `lab1_first_call.py` | Same prompt three times (are they the same?), and the `effort` knob with thinking tokens |
| ~11:14 | `tokens_minilab.py` | The same sentence in English, Hindi, Kannada and Tamil, counted |
| 11:41 | `lab2_cost.py` | The receipt (`usage`), cost per call and per month, the 100K cliff. Saves `results/week1_cost.txt` |
| 12:10 | `lab3_prompt_as_spec.py` | Your prompt as a versioned file you can `git diff` |
| 12:34 | `specs/triage_cli.md` | Live demo: spec first, then an AI coding agent builds it. You do it at home |
| stretch | `stretch_compare_models.py` | Haiku 5.5 vs Sonnet 5.5: is 20× the price 20× better? |
| demo (slide 24) | `demo_memory.py` | The model forgets: the same question without and with the conversation history |

`uv run lab1_first_call.py` sets everything up on the first run. No uv? `python -m venv .venv`, activate it, `pip install -r requirements.txt`, then `python lab1_first_call.py`.

Claude Code on the class key: `.\claude-class.cmd` (Windows) or `bash claude-class.sh` (macOS/Linux), from this folder. It uses your `.env` key and Haiku 5.5, and leaves your own Claude Code setup alone. Say **yes** when it asks to use the API key.

## Two things that will trip you up
- **A response is a list of blocks.** Haiku 5.5 thinks by default, so the first block may be `thinking`. Every lab picks text blocks by `type`.
- **`max_tokens` covers thinking + answer.** Set it too low and you can get thinking with no answer.

## Step-by-step pages
Open `exercises/index.html` in your browser: the morning's run-sheet, one page per lab, the checkpoint and the hand-in guide.

## Checkpoint (pass/fail, due Fri 4 Dec, 8 pm)
1. `results/week1_cost.txt` from `lab2_cost.py`, run with your own question.
2. `prompts/extract_ticket.md` at version v2, loaded by Lab 3.
3. `AI-NOTES.md`: one thing the AI got right, one it got wrong (from the homework build).
4. Pushed to your own private GitHub repo, tagged `wk1-checkpoint`, with `arunmariappan` added as a collaborator. Step by step: `exercises/handin.html`.
