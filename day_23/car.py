COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from random import choice, randint
import turtle as t

class Car:
    def __init__(self):
        self.color = choice(COLORS)
        self.ycor = randint(-300, 300)
        self.xcor = 300
        t.penup()
        t.shape("square")
        t.color(self.color)
        self.move()

    def move(self):
        if self.xcor > -300:
            self.xcor -= MOVE_INCREMENT
            t.goto(self.xcor, self.ycor)
