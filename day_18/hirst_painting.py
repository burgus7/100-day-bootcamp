import colorgram
import turtle
from random import choice

pen = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
pen.speed(0)

colors = colorgram.extract("reference_hirst_painting.jpg", 100)
screen.bgcolor(colors[0].rgb)


radius = 10
gap = 10
num_circles_x = 3
num_circles_y = 3

edge_x = num_circles_x*(radius*2+gap)
edge_y = num_circles_y*(radius*2+gap)

for x in range(-edge_x, edge_x, radius*2+gap):
    for y in range(-edge_y, edge_y, radius * 2 + gap):
        color = choice(colors)
        pen.color((color.rgb))
        pen.up()
        pen.goto(x, y)
        pen.down()
        pen.begin_fill()
        pen.circle(radius)
        pen.end_fill()

def draw_box():
    edge_x += gap
    edge_y += gap

    pen.penup()
    pen.goto(-edge_x-2*radius, -edge_y-2*radius)
    pen.color((0, 0, 0))
    pen.down()
    pen.goto(edge_x, -edge_y-2*radius)
    pen.goto(edge_x, edge_y)
    pen.goto(-edge_x-2*radius, edge_y)
    pen.goto(-edge_x-2*radius, -edge_y-2*radius)


screen.exitonclick()
