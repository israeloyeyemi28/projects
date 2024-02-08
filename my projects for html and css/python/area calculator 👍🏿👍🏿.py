

import math

shape = input("What shape would you like to calculate the area of? (rectangle, triangle, square, circle): ")

if shape == "rectangle":
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    area = width * height
    print("The area of the rectangle is:", area)

elif shape == "triangle":
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

elif shape == "square":
    side = float(input("Enter the length of a side of the square: "))
    area = side * side
    print("The area of the square is:", area)

elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print("The area of the circle is:", area)

else:
    print("Invalid shape entered. Please try again.")