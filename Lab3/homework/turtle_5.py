from turtle import *
# Turtle 5

def draw_star(x, y, length):
    penup()
    goto(x, y)
    for i in range(5):
        pendown()
        forward(length)
        penup()
        right(144)
    pendown()
