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
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(START_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


    def level_up(self):
        self.goto(START_POSITION)