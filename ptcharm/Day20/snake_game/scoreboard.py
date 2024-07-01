from turtle import Turtle

# 점수를 기록하는 방법과 출력하는 방법을 아는 터틀
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()