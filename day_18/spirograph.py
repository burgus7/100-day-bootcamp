import turtle
from turtle import Turtle, Screen
from random import choice, randint

pen = Turtle()
screen = Screen()

turtle.colormode(255)
screen.bgcolor((0, 0, 0))
pen.speed(9)

radius = 100
dist = 10
pen.pensize(3)

def random_color():
    r = randint(100, 255)
    g = randint(100, 255)
    b = randint(100, 255)
    return(r, g, b)

for _ in range(int(360 / dist)):
    pen.pencolor(random_color())
    pen.circle(radius)
    pen.left(dist)

screen.exitonclick()