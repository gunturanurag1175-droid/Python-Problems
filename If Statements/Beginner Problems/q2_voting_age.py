"""Ask the user for their age. Print "You are eligible to vote." if they are 18 or older, otherwise print "You are not eligible to vote yet."

💡 A simple if / else is enough here."""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")