# Lesson 6 of 12 - lists: several values, in order
#     uv run python_basics/06_lists.py

efforts = ["low", "medium", "high"]
print(efforts)
print(efforts[0])          # counting starts at 0, so [0] is the FIRST item
print(efforts[2])          # and [2] is the third
print(efforts[-1])         # -1 counts from the end: the last item
print(len(efforts))        # how many items

efforts.append("max")      # add an item to the end
print(efforts)
print("high" in efforts)   # is it in the list? True or False
print(efforts[1:3])        # a slice: items 1 and 2 (it stops BEFORE 3)

seconds = [1.2, 0.8, 2.5, 1.1]          # how long four calls took
print(sum(seconds), min(seconds), max(seconds))

# CHANGE ME: make a list of three tools you use at work, and print the second one.
