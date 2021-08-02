from turtle import Turtle, Screen
from random import choice

pen = Turtle()
screen = Screen()

edge_len = 100
colors = ["thistle1", "MediumPurple2", "maroon3", "gold2", "cyan", "peach puff", "deep sky blue", "dark turquoise"]

pen.pensize(4)
for i in range(3, 11):
    angle = 360/i
    pen.pencolor(choice(colors))
    for j in range(i):
        pen.forward(edge_len)
        pen.right(angle)

screen.exitonclick()