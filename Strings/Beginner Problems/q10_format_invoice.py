"""Store a customer name, item name, quantity (int), and price per unit (float) in variables. 
Print a neatly formatted invoice line like:
Customer: Alice | Item: Notebook x3 | Total: ₹150.00
using an f-string."""

customer = "Alice"
item = "Notebook"
quantity = 3
price = 50.0
total = quantity * price
print(f"Customer: {customer} | Item: {item} x{quantity} | Total: ₹{total:.2f}")