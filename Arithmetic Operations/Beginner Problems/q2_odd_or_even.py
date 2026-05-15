"""Ask the user to enter a number. Use the modulus operator % to check if it is odd or even, and print the result."""

num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Its an EVEN number.")
elif num % 2 == 1:
    print("Its an ODD number.")
else:
    print("Invalid number!")