"""Ask the user to enter a single character. Using or, check if it is a vowel (a, e, i, o, u) and print the result.
Do not use the in operator — use only or.

💡 ch == 'a' or ch == 'e' or ... — verbose but great practice for understanding or."""

ch = str(input("Enter a character: "))

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print(f"'{ch}' is a vowel.")
else:
    print(f"'{ch}' is not a vowel")