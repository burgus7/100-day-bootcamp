from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

difficulty = screen.textinput("Difficulty", "Enter 'easy', 'medium', or 'hard': ")
if difficulty == "hard":
    food_dist = 10
    speed = 0.05
elif difficulty == "easy":
    food_dist = 25
    speed = 0.15
else:
    food_dist = 15
    speed = 0.1

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < food_dist:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect Collision with Wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_over_msg = "You hit the wall."
        game_is_on = False

    # Detect collision with Tail
    if snake.tail_collision():
        game_over_msg = "You hit your tail."
        game_is_on = False

scoreboard.game_over(game_over_msg)
screen.exitonclick()

