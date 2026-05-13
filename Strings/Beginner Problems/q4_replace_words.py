"""Store the string "I like cats. Cats are great. My cat is named Luna.". 
Replace every occurrence of "cat" (case-insensitive) with "dog" and print the result."""

text = "I like cats. Cats are great. My cat is named Luna."
result = text.replace("cats", "dogs").replace("Cats", "Dogs").replace("cat","dog")
print(result)