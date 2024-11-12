'''
Write a program that prompts the user for a radius and then prints
•The area and circumference of a circle with that radius
•The volume and surface area of a sphere with that radius
'''

import math

# Ask user for the radius
radius = float(input("Enter the radius: "))

# Circle calculations
circle_area = math.pi * radius ** 2
circle_circumference = 2 * math.pi * radius

# Sphere calculations
sphere_surface_area = 4 * math.pi * radius ** 2
sphere_volume = (4 / 3) * math.pi * radius ** 3

# Results for the circle
print(f"\nFor a circle with radius {radius}:")
print(f"Area: {circle_area:.2f}")
print(f"Circumference: {circle_circumference:.2f}")

# Results for the sphere
print(f"\nFor a sphere with radius {radius}:")
print(f"Surface Area: {sphere_surface_area:.2f}")
print(f"Volume: {sphere_volume:.2f}")
