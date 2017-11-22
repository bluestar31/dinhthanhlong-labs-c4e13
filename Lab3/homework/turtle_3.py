from turtle import *

shape("turtle")

def draw_square(length, turtle_color):
    speed(-1)
    color(turtle_color)
    for i in range(4):
        forward(length)
        left(90)
