import turtle
from random import randint

screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.bgcolor("LightSkyBlue1")

is_race_on = False
cur = turtle.Turtle()
cur.color("black")
cur.pensize(3)
cur.penup()
cur.goto(x=200, y=-150)
cur.pendown()
cur.goto(x=200, y=150)
cur.color("LightSkyBlue1")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

start_x = -200
start_y = -125
for turt_color in colors:
    new_turt = turtle.Turtle()
    new_turt.shape("turtle")
    new_turt.color('black', turt_color)
    new_turt.penup()
    new_turt.goto(x=start_x, y=start_y)
    start_y += 50
    all_turtles.append(new_turt)

is_race_on = True
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

while is_race_on:
    for turt in all_turtles:
        rand_dist = randint(1, 10)
        turt.forward(rand_dist)
        if turt.xcor() > 200:
            winner = turt.color()[1]
            is_race_on = False

if winner == user_bet:
    user_win = True
else:
    user_win = False

cur.penup()
cur.home()
cur.color(winner)
cur.write(arg=f"{winner.title()} won!\nYou {'win' if user_win else 'lose'}", move=False, align="center", font=("Arial", 16, "bold"))
cur.color("LightSkyBlue1")

turtle.mainloop()

