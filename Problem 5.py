# Michelle Patlan
# 8/20/2022
# Problem 5: Use the following chunk of code as a base to produce the image shown below.

import turtle

#draws each square
def drawSquare(t, sz):
    # Get turtle t to draw a square of sz side""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")\

#global variable to get the sizing
side = 20
width = 10
for squares in range(5):

    #tells turtle to follow the function
    drawSquare(alex, side)
    alex.penup() #reposition the pen
    alex.back(width)
    alex.right(90)
    alex.forward(width)
    alex.left(90)
    alex.pendown()
    side+=2*width


wn.exitonclick()
