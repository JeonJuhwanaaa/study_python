from turtle import Turtle
from ball import Ball


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.goto(y=190, x=0)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} {self.r_score}", align="center", font=("Courier", 80, "normal"))

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
