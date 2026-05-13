"""Store the string "Learning Python is fun and Python is powerful". 
Find and print: the index of the first occurrence of "Python", the index of the last occurrence, and the total number of times it appears."""

text = "Learning Python is fun and Python is powerful"
print("First index:", text.find("Python"))
print("Last index:", text.rfind("Python"))
print("Count:", text.count("Python"))