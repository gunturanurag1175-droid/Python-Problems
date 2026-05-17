"""A smart thermostat turns ON the AC if:

• Temperature is above 30°C and it is daytime (yes/no)
• Or temperature is above 35°C regardless of time

Ask the user for the temperature and whether it is daytime. Print "AC turned ON." or "AC stays OFF."

💡 Combine and + or in one condition. Use parentheses to make the logic explicit and readable."""

temp = float(input("Enter temperature (°C): "))

if temp >= 35:
    print("AC turned ON.")
elif temp > 30:
    daytime = input("Is it daytime? (yes/no): ").lower() == "yes"
    if daytime:
        print("AC turned ON.")
    else:
        print("AC stays OFF.")
else:
    print("AC stays OFF.")