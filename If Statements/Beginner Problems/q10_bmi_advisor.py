"""Ask the user for their weight (kg) and height (m). Calculate their BMI. Then print a health category and a short message based on it:

BMI < 18.5 → Underweight
18.5 – 24.9 → Normal weight
25 – 29.9 → Overweight
30+ → Obese
💡 Combine arithmetic (**) and elif chains — a great mix of everything you've learned so far!"""

w = float(input("Enter weight (kg): "))
h = float(input("Enter height (m): "))
bmi = w / h ** 2

if bmi < 18.5:
    print(f"{bmi:.1f} - Under weight.")
elif 18.5 <= bmi <= 24.9:
    print(f"{bmi:.1f} - Normal weight.")
elif 25 <= bmi <= 29.9:
    print(f"{bmi:.1f} - Over weight.")
else:
    print(f"{bmi:.1f} - Obese.") 
