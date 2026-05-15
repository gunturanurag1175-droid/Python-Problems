"""Ask the user to enter a 3-digit number (e.g. 745). 
Using only // and %, extract and print each digit separately: hundreds, tens, and units."""

num = int(input("Enter a 3-digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10
print("Hundreds:", hundreds)
print("Tens:    ", tens)
print("Units:   ", units)