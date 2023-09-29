import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_new_car()
    cars.move()

    for car in cars.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.increase_level()
        cars.increase_car_speed()
        player.level_up()

screen.exitonclick()
