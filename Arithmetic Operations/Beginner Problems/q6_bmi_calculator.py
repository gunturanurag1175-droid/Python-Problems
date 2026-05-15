"""Ask the user for their weight in kg and height in metres. 
Calculate their BMI using the formula weight / height² and print it rounded to 2 decimal places."""

weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))

bmi = weight / height ** 2

print(f"Your BMI is:{bmi:.2f}")