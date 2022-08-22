# Michelle Patlan
# 8/20/2022
# Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Make sure you use the math module in your solution.


import math

#fomula pi * r sqrt
def area_of_circle(r):
    area_of_circle = r * r * math.pi
    return area_of_circle

#assigning radius r
r = 10

print("The area of the circle is", area_of_circle(r))