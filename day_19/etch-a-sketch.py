import turtle

cur = turtle.Turtle()
screen = turtle.Screen()

angle = 10
dist = 10

def move_forward():
    cur.forward(dist)

def move_back():
    cur.back(dist)

def turn_right():
    cur.right(angle)

def turn_left():
    cur.left(angle)

def clear_board():
    cur.clear()
    cur.penup()
    cur.home()
    cur.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear_board, "c")

turtle.mainloop()

