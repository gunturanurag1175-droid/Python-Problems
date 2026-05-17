"""Ask the user if it is raining (yes/no). Store the answer as a boolean. 
Using the not operator, print "Good day to go outside!" if it is not raining, otherwise print "Stay indoors."

💡 not True gives False and vice versa. Convert the input to a boolean first."""

answer = input("Is it raining? (yes/no): ").lower()
is_raining = answer == "yes"

if not is_raining:
    print("Good day to go outside!")
else:
    print("Stay indoors.")