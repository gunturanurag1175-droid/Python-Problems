"""Store a correct username and password in your code. 
Ask the user to enter both. Print "Login successful!" only if both match, "Wrong password." if the username is correct but password isn't,
and "Username not found." if the username is wrong.

💡 Use a nested if inside the outer if to check the password separately."""

username = "2310040031"
password = "KL@123"

req_username = (input("Enter Username: "))
req_pass = (input("Enter Password: "))
if req_username == username and req_pass == password:
    print("Login successful!")
elif req_username == username:   # password must be wrong, since first condition failed
    print("Wrong password.")
elif  req_pass == password:
    print("Wrong username.")
else:
    print("Username and Password are wrong!")