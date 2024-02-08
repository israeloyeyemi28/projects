
import math

print("Welcome to the tire volume program. This program calculates the volume of your tires... 🚗🛻🚙")

width = float(input("Enter the width of the tire (e.g., 205): "))
ratio = float(input("Enter the aspect ratio of the tire (e.g., 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g., 15): "))

volume = (math.pi * width**2 * ratio * (width * ratio + 2540 * diameter)) / 10000000000

print(f"The approximate volume of the tyre is {volume}")