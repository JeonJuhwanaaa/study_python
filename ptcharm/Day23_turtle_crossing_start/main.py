## 혼자서 만들어 본 것. (약 1시간 소요)

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up_move, "Up")
screen.onkey(player.down_move, "Down")

run_game = True

while run_game:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    if car_manager.xcor() > 290:
        car_manager.goto(-290, 0)

    if player.distance(car_manager) < 15:
        run_game = False
        scoreboard.game_over()

    if player.ycor() > 200:
        scoreboard.level_up()
        car_manager.level_up()
        player.level_up()


screen.exitonclick()


# 소요시간 : 약 1시간
# Move the turtle with keypress
# Create and Move the cars / JUST ONE
# Detect collision with car -> GAME OVER
# Detect when turtle reaches the other side -> LEVEL UP (SPEED UP)
# Create a scoreboard