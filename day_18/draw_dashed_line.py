from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

screen.screensize(1000, 200)
pen.up()
pen.goto(-500, 0)

for _ in range(50):
    pen.forward(10)
    pen.penup()
    pen.forward(10)
    pen.pendown()

screen.exitonclick()
