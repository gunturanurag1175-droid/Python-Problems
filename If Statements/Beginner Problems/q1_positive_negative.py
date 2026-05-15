"""Ask the user to enter a number. Print whether it is positive, negative, or zero.

💡 You'll need three branches — think if, elif, and else."""

number = int(input("Enter a number: "))
if number > 0:
    print("Positive Number.")
elif number < 0:
    print("Negative Number.")
else:
    print("Zero.")