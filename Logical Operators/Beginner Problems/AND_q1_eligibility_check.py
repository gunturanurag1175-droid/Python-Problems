"""Ask the user for their age and whether they have a valid ID (yes/no). Print "Entry allowed." only if they are 18 or older and have a valid ID.
Otherwise print "Entry denied."

💡 Both conditions must be True at the same time — that's exactly what and is for."""

age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()

if age >= 18 and has_id == "yes":
    print("Entry allowed.")
else:
    print("Entry denied.")