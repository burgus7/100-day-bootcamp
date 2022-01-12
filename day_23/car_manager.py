from random import randint
from car import Car
from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.collision_range_cars = []
        self.generation_speed = 5
        self.move_distance = STARTING_MOVE_DISTANCE
        self.scoreboard = Scoreboard()

    def make_car(self):
        """Make a new car from Car class, add to cars list"""
        rand_num = randint(0, self.generation_speed)
        if rand_num == 0:
            new_car = Car()
            self.cars.append(new_car)

    def manage_cars(self, player):
        """Loop through every car in list,
        either move or delete based on xcor"""

        cars_copy = []

        # loop cars
        for i in range(len(self.cars)):
            car = self.cars[i]

            # check collision
            if player.is_collision(car):
                return True

            # add visible cars
            if car.xcor > -330:
                car.xcor -= self.move_distance
                car.goto(car.xcor, car.ycor)
                cars_copy.append(car)

        # copy list back to original variable
        self.cars = cars_copy
        return False

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

