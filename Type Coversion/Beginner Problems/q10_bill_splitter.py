"""Ask the user for a total bill amount and number of people. 
Convert both inputs to the right types, calculate each person's share, and print it rounded to 2 decimal places."""

total_bill = float(input("Enter bill amount:"))
num_of_people = int(input("Enter number of people:"))
share_of_each_person = total_bill / num_of_people
print(f"The total Bill is {total_bill}, the number of people are {num_of_people} and each person's share is {share_of_each_person:.2f}")

