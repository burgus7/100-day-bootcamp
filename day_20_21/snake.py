from turtle import Turtle
START_POS = (0, 0)
MOVE_DIST = 20

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        start_length = 3
        for x in range(0, -20 * start_length, -20):
            self.add_segment((x + START_POS[0], START_POS[1]))


    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)


    def extend(self):
        self.add_segment(self.snake_body[-1].position())


    def tail_collision(self):
        for seg in self.snake_body[1:]:
            if self.head.distance(seg) < 15:
                return True
        return False


    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)


    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)


    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)


    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)






