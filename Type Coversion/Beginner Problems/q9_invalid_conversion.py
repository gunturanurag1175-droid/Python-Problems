"""Try converting the string "hello" to an integer. 
Wrap it in a try-except block and print a friendly message like 
"Oops! That can't be converted to a number." instead of crashing."""

try:
    result = int("hello")
except ValueError:
    print("Oops! That can't be converted to a number.")
    
