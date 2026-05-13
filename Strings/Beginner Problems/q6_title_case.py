"""Ask the user to enter their full name (e.g. "alice johnson"). 
Print it in title case, stripped of any extra spaces at the start or end."""

name = input("Enter your full name: ")
print(name.strip().title())