"""Ask the user for a base and an exponent. 
Calculate and print the result using the ** operator. Also print the square root of the base (use exponent 0.5)."""

base = float(input("Enter base: "))
exp = float(input("Enter exponent: "))
print("Result:     ", base ** exp)
print("Square root:", base ** 0.5)