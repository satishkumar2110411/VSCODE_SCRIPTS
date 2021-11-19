from math import pi
try:
    print("This program will print the area of circle with user input for radius")
    r = float(input("Enter radius: "))
    if r >= 0:
        area = pi*r**2
        print("For radius",r,"the area of circle is",area,"units squared.")
    else:
        print("Please enter valid value for radius.")
except Exception as e:
    print(e,"Please e1nter a valid value for radius")