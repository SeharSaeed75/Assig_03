# Assignment 03 
# Some basic problems.

# Calculate your age based on the current year and your birth year.
print("Age")
currrent_year = 2024
your_birthyear = int(input("Enter your_birthyear = "))
age = currrent_year - your_birthyear
print("Age = " ,age)
print("----------------------------------------------------------------- \n")

# Write a program that calculates the area of a rectangle using length and width variables.
print("Area of Rectangle")
length_rectangle = float (input("Enter length of rectangle = "))
width_rectangle = float (input("Enter width of rectangle = "))
area_rectangle = length_rectangle * width_rectangle
print("Area of Rectangle = " , area_rectangle )
print("----------------------------------------------------------------- \n")

# Write a program that calculates the area of a circle.
print("Area of Circle")
radius_circle = float (input("Enter the radius = "))
area_circle = (3.14159) * (radius_circle ** 2)
print("Area of Circle = " , area_circle )
print("----------------------------------------------------------------- \n")


# Write a program that calculates the area of the cube.
print("Area of Cube")
surface_area = float (input("Enter surface area = "))
area_cube = 6 * (surface_area ** 2)
print("Area of cube = " , area_cube )
print("----------------------------------------------------------------- \n")

# Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
print("Fahrenheit to Celsius")
F = float (input("Enter Temperature in Fahrenheit = "))
C = (F - 32) * 5/9
print("Celsius = " , C , "°C" )
print("\n")

print("Celsius to Fahrenheit")
Celsius = float (input("Enter Temperature in Celsius = "))
Fahrenheit = (Celsius * 9/5) + 32
print("Fahrenheit = " , Fahrenheit , "°F" )
print("----------------------------------------------------------------- \n")


# Convert a given number of seconds into minutes and seconds using variables.
print("Second into Minutes")
sec = float (input("Enter the seconds = "))
min = sec / 60
print("Minutes = " , min )
print("\n")

print("Minutes into Second")
minutes = float (input("Enter the Minutes = "))
second = (minutes * 60)
print("Seconds = " , second )
print("----------------------------------------------------------------- \n")

# Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
print("Body Mass Index")
height_BMI = float (input("Enter the Height (in meter) = "))
weight_BMI = float (input("Enter the Weight (in Kg) = "))
bmi = weight_BMI / (height_BMI ** 2)
print("Body Mass Index = " , bmi )
print("----------------------------------------------------------------- \n")


# Write a program that calculates the volume of a cylinder using the formula.
print("Volume of Cylinder")
radius_cylinder = float (input("Enter radius of Cylinder = "))
height_cylinder = float (input("Enter Height of Cylinder = "))
volume_cylinder = (3.14159) * (radius_cylinder ** 2) * height_cylinder
print("Volume of Cylinder = " , volume_cylinder )
print("----------------------------------------------------------------- \n")