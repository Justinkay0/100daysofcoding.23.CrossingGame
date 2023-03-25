import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
leo = Player()
scoreboard = Scoreboard()
vehicles = []

game_is_on = True
screen.listen()


while game_is_on:
    if random.randint(0, 100) > 75:
        car = CarManager()
        vehicles.append(car)
    screen.onkey(leo.moving, 'Up')

    if leo.ycor() >= 280:
        leo.new_level()
        scoreboard.update()

    for cars in vehicles:
        cars.car_moving(scoreboard.level)
        if leo.distance(cars) < 20:
            game_is_on = False
    time.sleep(0.1)
    screen.update()


scoreboard.game_over()
screen.exitonclick()
