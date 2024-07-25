from turtle import Turtle

FONT = ("Courier", 24, "normal")


# 게임 레벨 관리 및 게임오버 알림 클래스
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Label: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()