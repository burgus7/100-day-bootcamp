import turtle
from turtle import Turtle, Screen
from random import choice, randint

pen = Turtle()
screen = Screen()

turtle.colormode(255)
screen.bgcolor((0, 0, 0))
pen.speed(3)
walk_len = 20
directions = [0, 90, 180, 270]
pen.pensize(10)

def random_color():
    r = randint(100, 255)
    g = randint(100, 255)
    b = randint(100, 255)
    return(r, g, b)

while True:
    pen.pencolor(random_color())
    direction = choice(directions)
    pen.seth(direction)
    pen.forward(walk_len)


screen.exitonclick()