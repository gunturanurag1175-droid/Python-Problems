"""A bank approves a loan only if the applicant's age is between 21 and 60 (inclusive) and their monthly income is at least ₹25,000. 
Ask for both values and print "Loan approved." or "Loan rejected."

💡 Use chained comparison for age: 21 <= age <= 60, combined with and for income."""

age = int(input("Enter Age: "))
monthly_income = float(input("Enter Monthly Income: "))

if 21 <= age <= 60 and monthly_income >= 25000:
    print("Loan Approved.")
else:
    print("Loan Rejected.")