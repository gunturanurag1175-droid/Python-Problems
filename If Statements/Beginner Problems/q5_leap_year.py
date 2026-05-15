"""Ask the user to enter a year. Determine whether it is a leap year and print the result.

A year is a leap year if: it is divisible by 4 AND (not divisible by 100 OR divisible by 400).

💡 Use and / or logical operators along with % to check divisibility."""

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")