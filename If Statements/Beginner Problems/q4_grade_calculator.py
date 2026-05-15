"""Ask the user for a score out of 100. Print the corresponding grade:

90–100 → A  |  80–89 → B  |  70–79 → C  |  60–69 → D  |  below 60 → F

💡 Use a chain of elif statements. Check from highest to lowest."""

score = int(input("Enter a score (out of 100): "))

if 90 <= score <= 100:   # Python allows chained comparisons!
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif score < 60:
    print("F")
else:
    print(f"Invalid score! {score} is not between 0 and 100.")