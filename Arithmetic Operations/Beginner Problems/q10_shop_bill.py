"""A shop sells items. Ask the user for the price per item, quantity bought, and a discount percentage. 
Calculate and print: the subtotal, discount amount, and final price after discount — all formatted to 2 decimal places."""

p = float(input("Enter the price per item: "))
q = int(input("Enter the quantity: "))
d = float(input("Enter the discount (%): "))
subtotal = p * q
discount = subtotal * d / 100
final_price = subtotal - discount
print(f"Subtotal:        ₹{subtotal:.2f}")
print(f"Discount ({d}%): ₹{discount:.2f}")
print(f"Final price:     ₹{final_price:.2f}")

