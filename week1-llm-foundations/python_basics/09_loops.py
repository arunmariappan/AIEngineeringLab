# Lesson 9 of 12 - for loops: do the same thing for each item
#     uv run python_basics/09_loops.py

for effort in ["low", "medium", "high"]:
    print("trying effort", effort)        # runs once per item; `effort` holds the current one

for run in range(1, 4):                   # 1, 2, 3: range stops BEFORE 4
    print(f"run {run}")

usage = {"input_tokens": 31, "output_tokens": 52}
for label, value in usage.items():        # a dict gives you each label and its value
    print(label, "->", value)

total = 0
for count in [12, 30, 8, 2]:
    total = total + count                 # add up as you go
print("tickets today:", total)

tickets = {"low": 12, "medium": 30, "high": 8, "urgent": 2}
for priority, count in tickets.items():
    if count < 10:                        # an if inside a loop: keep only some items
        print(f"only {count} {priority} tickets")

# CHANGE ME: loop over a list of three foods you like, and print each one in an f-string.
