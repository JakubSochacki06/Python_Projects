import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

s = Screen()
s.bgcolor("gray")
s.setup(width=600, height=600)
s.tracer(0)

player = Player()

s.listen()
s.onkey(player.move_up , "Up")


game_is_on = True
car_list = []
scoreboard = Scoreboard()
while game_is_on:
    time.sleep(0.1)
    s.update()
    toss = random.randint(0 , 3)
    if toss == 0:
        car = CarManager()
        car_list.append(car)
    else:
        pass
    for car in car_list:
        car.move()
    if player.check_position() == True:
        scoreboard.increase_score()
        car.increase_speed()

    for car in car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

s.exitonclick()