"""Ask the user for a principal amount, annual interest rate (as a percentage), and number of years. 
Calculate simple interest using SI = (P × R × T) / 100 and print the interest and total amount."""

p = float(input("Principal amount: "))
r = float(input("Annual rate (%): "))
t = float(input("Time (years): "))
si = (p * r * t) / 100
print(f"Simple Interest: ₹{si:.2f}")
print(f"Total Amount:    ₹{p + si:.2f}")