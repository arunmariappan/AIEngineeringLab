# Lesson 5 of 12 - numbers and the Week 1 cost formula
#     uv run python_basics/05_numbers.py

print(7 + 3, 7 - 3, 7 * 3)   # add, subtract, multiply
print(7 / 2)                 # divide: / always gives a decimal
print(7 // 2)                # whole-number divide: drops the remainder
print(7 % 2)                 # the remainder
print(2 ** 10)               # "to the power of"

# Haiku 5.5 prices are in dollars per MILLION tokens: $0.10 in, $0.50 out.
input_tokens = 2_000         # underscores make big numbers easier to read; Python ignores them
output_tokens = 400
cost = input_tokens / 1_000_000 * 0.10 + output_tokens / 1_000_000 * 0.50
print(cost)                  # computers store decimals approximately, so you may see many digits
print(round(cost, 6))        # rounded to 6 decimal places
print(f"${cost:.6f}")        # :.6f in an f-string = always show 6 decimal places

calls_per_month = 10_000 * 5 * 30
print(f"{calls_per_month:,} calls a month")            # :, adds commas
print(f"${cost * calls_per_month:,.2f} a month")       # commas AND 2 decimal places

# CHANGE ME: price a 120,000-token prompt. Over 100K tokens the input rate is $0.50 per million.
