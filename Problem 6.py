

from turtle import *
#import everything in turtle
color("pink")
pensize(4)

#drawing the shape
for i in range (10):
    for p in range(5): #for p in range(6)- hexagon has six sides
        right(72)      #right(60) <= 360/6 = 60
        forward(100)
    right(45)  #right(36) <==  360/10
