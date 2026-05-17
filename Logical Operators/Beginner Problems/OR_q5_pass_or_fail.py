"""A student passes if their score is 50 or above or they have submitted extra credit (yes/no). Ask for both and print "Pass" or "Fail".

💡 Even a score of 30 passes if extra credit is yes — only one condition needs to be True with or."""


score = int(input("Enter your score: "))
extra_credit = input("Submitted extra credit? (yes/no): ").lower()

if score >= 50 or extra_credit == "yes":
    print("Pass.")
else:
    print("Fail.")