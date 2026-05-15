"""Ask the user to enter three numbers. Find and print the largest one using if / elif / else.

💡 Compare the first number against the other two, then handle ties if needed."""

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 >= num2 and num1 >= num3:
    print("1st number is largest one.")
elif num2 >= num1 and num2 >= num3:
    print("2nd number is the largest one.")
else:
    print("3rd number is the largest one.")