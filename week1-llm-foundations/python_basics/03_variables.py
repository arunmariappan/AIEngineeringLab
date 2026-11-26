# Lesson 3 of 12 - variables: a name for a value
#     uv run python_basics/03_variables.py

model = "claude-haiku-5-5"      # = puts the value on the right into the name on the left
max_tokens = 1024
print(model)
print(max_tokens)

max_tokens = 2048               # a variable can change: the name now holds a new value
print(max_tokens)

learners = 9
pairs = 4
print(learners - pairs * 2)     # 9 - 8 = 1 learner left over, who makes one pair a trio

print(learners == 9)            # == ASKS "is it equal?" and answers True or False
print(learners == 10)

# Good names: lowercase_with_underscores, no spaces, never starting with a digit.
# CAPITALS (like MODEL in the labs) mean "set once, don't change it".

# CHANGE ME: make a variable called my_name, put your name in it, and print it.
