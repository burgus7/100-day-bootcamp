import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()
    screen.bgcolor("lightblue")

    player = Player()
    score_board = Scoreboard()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(player.move, "Up")

    #score_board.countdown(screen)

    game_is_on = True
    while score_board.is_game_on:
        time.sleep(0.1)
        car_manager.make_car()

        is_collision = car_manager.manage_cars(player=player)

        if is_collision:
            score_board.game_over()

        # leveling up
        if player.is_finish():
            player.reset_position()
            score_board.level_up()
            car_manager.increase_speed()


        screen.update()

