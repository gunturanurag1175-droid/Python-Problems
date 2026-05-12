"""Write a program that counts how many vowels (a, e, i, o, u) are in the string "I love programming".
Print the count."""

text = "I love programming"
count = 0
for char in text.lower():
    if char in "aeiou":
        count += 1
print("Vowel count:", count)