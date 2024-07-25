from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPEED = 10


# 자동차가 랜덤으로 나오게 하는 클래스
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1 ,stretch_len=2)
        self.goto(0, 0)

    def move(self):
        x = self.xcor() + SPEED
        self.goto(x, self.ycor())

    def level_up(self):
        global SPEED
        SPEED += 3
