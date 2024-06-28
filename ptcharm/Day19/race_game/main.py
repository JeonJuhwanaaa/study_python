from turtle import Turtle, Screen
import random


screen = Screen()

# setup() -> 표시되는 창의 폭와 높이를 설정 / 인수는 (폭, 높이)
# 포인트 좌표를 지정하려면 크기가 중요하다.
screen.setup(width=500, height=400)

# textinput() / numinput() -> 팝업창을 띄워 사용자가 메세지와 제목을 읽고 텍스트 또는 숫자를 입력받는다.
user_bet = screen.textinput(title="내기를 걸어보세요.", prompt="어떤 거북이가 이길까요? 색을 골라주세요: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_index = [-70, -40, -10, 20, 50, 80]

# tim = Turtle(shape="turtle")  # 이렇게도 shape 정의 가능
# tim.shape("turtle")
# tim.color(colors[0])
# tim.penup()
# tim.goto(x=-230, y=-100)
#
# tom = Turtle(shape="turtle")
# tom.color(colors[1])
# tom.penup()
# tom.goto(x=-230, y=-70)
#
# tum = Turtle(shape="turtle")
# tum.color(colors[2])
# tum.penup()
# tum.goto(x=-230, y=-40)
#
# tin = Turtle(shape="turtle")
# tin.color(colors[3])
# tin.penup()
# tin.goto(x=-230, y=-10)
#
# til = Turtle(shape="turtle")
# til.color(colors[4])
# til.penup()
# til.goto(x=-230, y=20)
#
# tun = Turtle(shape="turtle")
# tun.color(colors[5])
# tun.penup()
# tun.goto(x=-230, y=50)

# ------------------------------------------------------------------------------

is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # 이렇게도 shape 정의 가능
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_index[turtle_index])
    all_turtles.append(new_turtle)

if user_bet: # user_bet 가 존재한다면
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230: # x좌표
            is_race_on = False
            # print(turtle.color()) # 첫번째 색상은 펜의 색상, 두번재는 채우기 색상
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()