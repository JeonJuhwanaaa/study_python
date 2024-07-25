import turtle
from turtle import Turtle, Screen
import random


#  turtle 문서 참고 사이트 -> https://docs.python.org/3/library/turtle.html
# color 사이트 -> https://trinket.io/docs/colors

# GUI - graphical user interface

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed(2)

# timmy_the_turtle.color("blue")


# 거북이 정사각형 만들기

def left():
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)

timmy_the_turtle.forward(100)
left()
left()
left()

# 다른 방법

for move in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

# ---------------------------------------------

# 거북이로 거미줄 만들기

for steps in range(101):
    for c in ("blue", "red", "green"):
        timmy_the_turtle.color(c)
        timmy_the_turtle.forward(steps)
        timmy_the_turtle.right(30)

# ---------------------------------------------

# 점선 그리기

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.color("white")
    timmy_the_turtle.forward(10)
    timmy_the_turtle.color("black")

# 다른 방법

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup() # 선을 그리지 않고 앞으로 이동 시킨다.
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

# ---------------------------------------------

# 삼각형부터 도형이 커지면서 그리기
# 도형이 커질수록 변의 수가 1씩 늘고 각도는 360 / 변의수

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(360 / num_sides)

for shape_side_n in range(3, 11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
#
# timmy_the_turtle.left(72)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(72)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(72)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(72)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(72)
# timmy_the_turtle.forward(100)

# ---------------------------------------------

# random walk - 랜덤으로 방향정해서 이동, 색 랜덤 변경, 선 굵기 변경하기

# 각도 방향 : 0도 - east / 90 - north / 180 - west / 270 - south
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed(5)

# 내가 한 것.

for _ in range(50):
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.left(random.choice(directions))

# 강의에서 한 것.

for _ in range(200):
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.forward(30)
    # setheading() 함수는 -> 거북이의 머리 방향을 지정하는 데 사용됩니다.
    timmy_the_turtle.setheading(random.choice(directions))


# ---------------------------------------------

# 튜플로 RGB 색상 랜덤 돌리기

turtle.colormode(255) # 0 ~ 255 까지 색상 범위 설정
def random_color():
    r = random.randint(0, 255) # 레드
    g = random.randint(0, 255) # 그린
    b = random.randint(0, 255) # 블루
    random_color = (r, g, b) # 튜플로 rgb 색상 랜덤 고르기
    return random_color

for _ in range(200):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    # setheading() 함수는 -> 거북이의 머리 방향을 지정하는 데 사용됩니다.
    timmy_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()