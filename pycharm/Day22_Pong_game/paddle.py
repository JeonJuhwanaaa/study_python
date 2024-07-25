from turtle import Turtle

class Paddle(Turtle):
    
    moving_up = False

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1) # 패들의 크기
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)
    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)