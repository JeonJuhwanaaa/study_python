from turtle import Turtle

START_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

# 거북이를 이동하게 하는 클래스
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)

    def up_move(self):
        self.forward(MOVE_DISTANCE)

    def down_move(self):
        self.backward(MOVE_DISTANCE)

    def level_up(self):
        self.goto(START_POSITION)