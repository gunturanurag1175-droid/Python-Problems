"""Ask the user to enter a number. 
Print "FizzBuzz" if it is divisible by both 3 and 5, "Fizz" if divisible only by 3, 
"Buzz" if divisible only by 5, or the number itself if none of the above.
💡 Check the combined condition first — order matters here!
"""

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
