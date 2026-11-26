# Lesson 10 of 12 - functions: name a recipe, use it many times
#     uv run python_basics/10_functions.py

def cost_usd(input_tokens, output_tokens):
    """Dollar cost of one Haiku 5.5 call (prompt under 100K tokens)."""
    return input_tokens / 1_000_000 * 0.10 + output_tokens / 1_000_000 * 0.50


print(cost_usd(2000, 400))                               # give it values in order...
print(cost_usd(output_tokens=400, input_tokens=2000))    # ...or by name: same answer


def greet(name, greeting="Hello"):        # greeting has a default, so you can leave it out
    return f"{greeting}, {name}!"


print(greet("Asha"))
print(greet("Asha", greeting="Vanakkam"))


def shout(text):
    print(text.upper())                   # this PRINTS, but doesn't RETURN anything


result = shout("done")
print(result)                             # None: there was nothing returned to keep

# CHANGE ME: write a function monthly_cost(cost_per_call, calls) that returns
# cost_per_call * calls, then print monthly_cost(0.0004, 1_500_000).
