import time
from turtle import Screen

import scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

score = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")


car = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    for carr in car.all_cars:
        if carr.distance(player) < 20 or screen.onkey(score.quit, "q"):
            game_is_on = False
            score.game_over()

    if player.is_at_finsh_line():
        player.go_to_start()
        car.increase_speed()
        score.inc_score()


screen.exitonclick()