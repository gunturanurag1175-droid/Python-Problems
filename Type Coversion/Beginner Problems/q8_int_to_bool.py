"""Ask the user to enter a number. Convert it to an integer, then to a boolean. 
Print whether the number is truthy or falsy."""

num = int(input("Enter a number:", ))
result = bool(num)
if result:
    print(num, "is truthy")
else:
    print(num, "is falsy")