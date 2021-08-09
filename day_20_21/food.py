from turtle import Turtle
from random import randint, choice

COLOR_PALETTE = ["purple", "blue", "yellow", "orange", "cyan", "magenta", "pink", "red", "green"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        rand_color = choice(COLOR_PALETTE)

        self.color(rand_color)
        self.goto(rand_x, rand_y)