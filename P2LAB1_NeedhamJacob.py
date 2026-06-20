# Jacob Needham
# 06/19/26
# P2LAB1
# Python code to Calculate Diameter, Circumference and area of a Circle

#Inported math module to use the constant, math.pi
import math

#User inputs Float number
#Ask user for Radius of the Circle

radius = float(input(
    "What is the Radius of the Circle? "
))
print()

#calculate the diameter
diameter = 2 * radius

#display the found diameter with 1 decimal point
print(
    f"The Diameter of the Circle is {diameter:.1f}\n"
)

#Calculate the Circumferece
circumference = 2 * math.pi * radius

#Display the Circumferance with 2 decimal points
print(
    f"The Circumference of the Circle is {circumference:.2f}\n"
)

#Calculate the Area of the Circle
area = math.pi * radius**2 

#Display the area with 3 decimals
print(
    f"The Area of the Circle is {area:.3f}"
)
