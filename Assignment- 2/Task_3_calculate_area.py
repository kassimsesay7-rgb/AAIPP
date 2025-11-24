'''Task Description #3
    • Ask Gemini to explain a Python function (to calculate area of various shapes) line by line..'''


import math

def calculate_area(name):
    """
    Calculates the area of various shapes based on user input.
    """
    name = name.lower()

    if name == "rectangle":
        l = float(input("Enter rectangle's length: "))
        w = float(input("Enter rectangle's width: "))
        rect_area = l * w
        print(f"The area of the rectangle is {rect_area}")

    elif name == "circle":
        r = float(input("Enter circle's radius: "))
        circ_area = math.pi * r**2
        print(f"The area of the circle is {circ_area}")

    elif name == "triangle":
        b = float(input("Enter triangle's base length: "))
        h = float(input("Enter triangle's height: "))
        tri_area = 0.5 * b * h
        print(f"The area of the triangle is {tri_area}")

    else:
        print("Sorry! This shape is not recognized.")

# Example function call:
calculate_area("Rectangle")




