"""Ask the user to enter a word. 
Check if it is a palindrome (reads the same forwards and backwards) and print "Yes, it's a palindrome!" or "No, it's not a palindrome."""

word = input("Enter a word: ").lower()
if word == word[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")