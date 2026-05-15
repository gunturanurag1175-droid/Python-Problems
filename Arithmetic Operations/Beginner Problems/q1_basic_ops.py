"""Take two numbers from the user and print the result of all 7 arithmetic operations on them: +, -, *, /, //, %, and **. 
Label each result clearly."""

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
floorDiv = num1 // num2
mod = num1 % num2
power = num1 ** num2
print(f"The result of all 7 arithmetic operations are:\nAdd = {add}\nSubtract = {sub}\nMultiply = {mul}\nDivide = {div}\nFloor Division = {floorDiv}\nModulus = {mod}\nPower = {power}")
