from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()
timmy.shape("turtle")
timmy.color("MediumPurple3")

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


screen.exitonclick()

