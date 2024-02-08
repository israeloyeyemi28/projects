print('welcome to my area calculator')
print('i hope you like it')
shape = input('what shape would you like to calculate? :')
if shape == "rectangle" :
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the lenght of the rectangle"))
    area = width * lenght
    print(f"The are of the rectangle is",area)
elif shape == "triangle":
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is",area)

elif shape == "square":
    side = float(input("Enter the length of a side of the square: "))
    area = side * side
    print(f"The area of the square is",area)

elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is",area)

elif shape == "pyramid" :
    base = float(input("Enter the base lenght of the pyramid :"))
    height = float(input("Enter the height of the pyramid :"))
    area = 1/3 * base * height    
    print(f"The area of the pyramid is",area)
    
    
else:
    print("Invalid shape entered. Please try again.")