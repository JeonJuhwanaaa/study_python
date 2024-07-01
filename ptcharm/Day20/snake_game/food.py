from turtle import Turtle
import random

class Food(Turtle): # turtle 상속 받기

    def __init__(self):
        super().__init__() # 상속받은 클래스를 사용
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refesh()
        

    # 뱀의 머리가 food 에 닿을 때 food 위치 랜덤으로 다시 생성
    def refesh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)