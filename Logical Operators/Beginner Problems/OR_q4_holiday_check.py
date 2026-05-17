"""Ask the user to enter a day of the week (e.g. Monday). Print "It's a holiday!" if the day is Saturday or Sunday, otherwise print "It's a working day."

💡 Use .lower() or .capitalize() so the check works regardless of how the user types the day."""

day = input("Enter day of the week: ").capitalize()

if day == "Saturday" or day == "Sunday":
    print("It's a holiday!")
else:
    print("It's a working day.")