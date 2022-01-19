from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.rand_color = choice(COLORS)
        self.ycor = randint(-250, 250)
        self.xcor = 300
        self.penup()
        self.shape("square")
        self.color(self.rand_color)

        self.resizemode("user")
        self.shapesize(1, 2, 1)

    #TODO Remove
    def is_collision(self, player):
        width_buffer = 40
        min_x = self.xcor - width_buffer
        max_x = self.xcor + width_buffer
        min_y = self.ycor - width_buffer/2
        max_y = self.ycor + width_buffer/2

        if min_x < player.xcor < max_x and min_y < player.ycor < max_y:
            return True
        return False

