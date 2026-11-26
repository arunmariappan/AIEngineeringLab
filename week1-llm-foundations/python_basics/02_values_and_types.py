# Lesson 2 of 12 - values and their types
#     uv run python_basics/02_values_and_types.py

print(type("hello"))        # str   = text. Always inside quotes.
print(type(42))             # int   = a whole number
print(type(0.10))           # float = a number with a decimal point
print(type(True))           # bool  = True or False (capital T, capital F)

# The type decides what + does:
print("42" + "8")           # two pieces of text, joined: 428
print(42 + 8)               # two numbers, added: 50

# Convert when you need to:
print(int("42") + 8)        # text -> number, then add: 50
print(str(42) + " tokens")  # number -> text, then join: 42 tokens

# CHANGE ME: add the line   print("42" + 8)   and run it.
# Read the error (a TypeError), then delete the line again.
