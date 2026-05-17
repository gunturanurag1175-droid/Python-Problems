"""A system gives access if the user is an admin or if they are a member and their account is active.
Ask for three inputs: is_admin, is_member, is_active (all yes/no). Print "Access granted." or "Access denied."

💡 Be careful about operator precedence — and is evaluated before or, just like * before + in arithmetic."""

is_admin  = input("Are you an admin? (yes/no): ").lower() == "yes"
is_member = input("Are you a member? (yes/no): ").lower() == "yes"
is_active = input("Is your account active? (yes/no): ").lower() == "yes"

if is_admin or (is_member and is_active):
    print("Access granted.")
else:
    print("Access denied.")
