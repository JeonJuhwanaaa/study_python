import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# key binding -------------------------------------
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

run_game = True

while run_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    # 뱀의 머리가 먹이에서 15픽셀 이내로, 혹은 그보다 더 가까운 거리에 있다면
    # (먹이 크기가 10x10 이니깐 여유를 둬서 15 로 설정)
    if snake.segments[0].distance(food) < 15:
        # print("nom nom nom")
        food.refesh()
        scoreboard.update_scoreboard()
        scoreboard.increase_score()


screen.exitonclick()