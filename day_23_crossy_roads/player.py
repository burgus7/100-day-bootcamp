from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.seth(90)

    def is_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_collision(self, car):
        width_buffer = 40
        min_x = self.xcor() - width_buffer
        max_x = self.xcor() + width_buffer
        min_y = self.ycor() - width_buffer/2
        max_y = self.ycor() + width_buffer/2

        if min_x < car.xcor < max_x and min_y < car.ycor < max_y:
            return True
        return False

    def reset_position(self):
        self.goto(STARTING_POSITION)

