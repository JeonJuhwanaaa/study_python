from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1 # 공이 위, 아래 벽에 닿았을 때 반대 방향으로 튕기기.

    def bounce_x(self):
        self.x_move *= -1 # 공이 패들에 닿았을 때 반대 방향으로 튕기기.