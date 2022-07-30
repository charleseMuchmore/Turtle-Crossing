import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
list_cars = []
for x in range(0, 100):
    x = CarManager()
    list_cars.append(x)




screen.listen()
screen.onkeypress(player.move, "Up")
screen.tracer(True)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in list_cars:
        car.move()

