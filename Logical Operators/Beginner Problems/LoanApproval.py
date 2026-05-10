# AND OPERATION
has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
    print("Approved for Loan!")
else: 
    print("Not Eligible for Loan.")

# OR OPERATION
has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Approved for Loan!")
else: 
    print("Not Eligible for Loan.")


# NOT OPERATION
has_high_income = True
has_criminal_record = False
if has_high_income and not has_criminal_record:
    print("Approved for Loan!")
else: 
    print("Not Eligible for Loan.")