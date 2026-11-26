# Lesson 8 of 12 - if / elif / else: making decisions
#     uv run python_basics/08_if.py

monthly_cost = 600
budget = 500
if monthly_cost > budget:
    print("Over budget: ask before you ship")
else:
    print("Within budget")

priority = "high"
if priority == "urgent":
    print("Page the on-call engineer")
elif priority == "high":
    print("Handle it today")
else:
    print("Add it to the queue")

prompt_tokens = 120_000
is_long = prompt_tokens > 100_000       # a comparison gives True or False
print(is_long)
if is_long and priority != "low":
    print("Long prompt: every rate is x5")

# Compare with:  ==  !=  <  >  <=  >=      Combine with:  and  or  not
# The indented lines belong to the line above them that ends with a colon.

# CHANGE ME: set priority to "urgent" and run; then to "low" and run again.
