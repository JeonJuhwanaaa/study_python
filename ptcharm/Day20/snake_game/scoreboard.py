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

    def game_over(self):
        self.goto(0, 0) # 게임이 끝나면 GAME OVER 라는 글이 가운데에서 보이게 하기.
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()