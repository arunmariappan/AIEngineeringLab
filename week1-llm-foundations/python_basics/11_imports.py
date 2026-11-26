# Lesson 11 of 12 - import: use code someone else wrote
#     uv run python_basics/11_imports.py

import math                      # a module (a toolbox) that comes with Python
import statistics
from datetime import date        # bring in just one name from a module

print(math.sqrt(16))             # module name, a dot, then the tool you want
print(math.ceil(2.1))            # round UP to a whole number
print(statistics.mean([1.2, 0.8, 2.5, 1.1]))    # the average of four call times
print(date(2026, 11, 28).strftime("%A"))    # which day of the week is Week 1?

# Packages that DON'T come with Python are installed first, then imported the same way.
# The labs use two, listed in pyproject.toml, and `uv run` installs them for you:
#     from anthropic import Anthropic
#     from dotenv import load_dotenv

# CHANGE ME: import the random module and print random.choice(["low", "medium", "high"]).
# Run it a few times: the answer changes, a bit like a model's.
