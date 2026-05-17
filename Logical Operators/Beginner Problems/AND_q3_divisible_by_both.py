"""Ask the user to enter a number. Check if it is divisible by both 3 and 7. Print "Divisible by both 3 and 7" or "Not divisible by both."

💡 Use % to check divisibility: num % 3 == 0 and num % 7 == 0."""

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both.")