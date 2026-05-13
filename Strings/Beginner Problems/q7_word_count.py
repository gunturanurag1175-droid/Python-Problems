"""Ask the user to type a sentence. Count and print the number of words in it."""

sentence = input("Type a sentence: ")
words = sentence.split()
print("Word count:", len(words))