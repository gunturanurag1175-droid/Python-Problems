"""Without running the code, predict the output of each line. Then run it and verify:

print(True and False)
print(True or False)
print(not True)
print(not False and True)
print(True and True or False)
print(not (True or False))

💡 Precedence order: not first, then and, then or. Brackets override everything."""

print(True and False)           # False — both must be True
print(True or False)            # True  — at least one is True
print(not True)                 # False — flipped
print(not False and True)       # True  — not False → True, True and True → True
print(True and True or False)   # True  — (True and True) → True, True or False → True
print(not (True or False))      # False — (True or False) → True, not True → False