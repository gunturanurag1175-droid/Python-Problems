"""Ask the user to enter the three angles of a triangle. 
First check if they form a valid triangle (angles must sum to 180). 
If valid, classify it as acute (all angles < 90), right (one angle = 90), or obtuse (one angle > 90).
💡 Use and to check all angles at once: a < 90 and b < 90 and c < 90."""


a = float(input("Angle 1: "))
b = float(input("Angle 2: "))
c = float(input("Angle 3: "))

if a + b + c == 180:
    if a == 90 or b == 90 or c == 90:
        print("Right triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse triangle")
    else:
        print("Acute triangle")
else:
    print("Not a valid triangle (angles don't sum to 180)")