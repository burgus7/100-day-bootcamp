STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super.__init__()
        self.goto(STARTING_POSITION)

    def is_finish(self):
        if self.ycor() >= 280:
            print ("DONE")
            return True
        else:
            return False

    def move(self):
        if not self.is_finish():
            self.forward(MOVE_DISTANCE)
