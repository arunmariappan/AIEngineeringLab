# Lesson 4 of 12 - strings: working with text
#     uv run python_basics/04_strings.py

ticket = "  Export button throws 500 for PAID users  "
print(len(ticket))                       # how many characters, spaces included
print(ticket.strip())                    # without the spaces at both ends
print(ticket.lower())                    # all lower case
print(ticket.replace("500", "an error")) # swap one piece of text for another
print("500" in ticket)                   # is this text inside? True or False

name = "Asha"
tokens = 1200
print(f"{name} used {tokens} tokens")    # an f-string: the {blanks} get filled in
print(f"That's {tokens / 1000} thousand tokens")   # any sum works inside { }

prompt = """You are a support-ticket triage assistant.
Return exactly three lines."""
print(prompt)                            # triple quotes hold text over several lines, like a prompt

# CHANGE ME: put your own name in `name`, then print one sentence about yourself with an f-string.
