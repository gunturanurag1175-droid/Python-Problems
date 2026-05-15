"""A cinema charges ticket prices based on age and day:

• Age under 5 → Free
• Age 5–17 → ₹100 on weekdays, ₹150 on weekends
• Age 18+ → ₹200 on weekdays, ₹300 on weekends

Ask the user for their age and whether it's a weekend (yes/no). Print the ticket price.
💡 Use nested if statements — check age first, then day inside."""

age = int(input("Enter age: "))
weekend = input("Is it a weekend? (yes/no): ").lower()

if age < 5:
    print("Ticket price: Free")
elif age <= 17:
    if weekend == "yes":
        print("Ticket price: ₹150")
    else:
        print("Ticket price: ₹100")
else:
    if weekend == "yes":
        print("Ticket price: ₹300")
    else:
        print("Ticket price: ₹200")