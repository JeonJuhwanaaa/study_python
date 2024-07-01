from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600, height=600) # 창 크기 설정
screen.bgcolor("black") # 배경 색 설정
screen.title("Snake Game") # 게임 제목
# tracer 메소드 -> 터틀 그래픽의 자동 업데이트를 제어하고, 애니메이션의 속도를 조절 가능
# 매개변수 1 이면 모든 움직임이 즉시 화면에 반영 / 0 이면 애니메이션이 비활성화
screen.tracer(0)

# 첫단계, 네모모양 / 20x20 크기 / 화이트색상 / 3개 나열
# 내가 한 것.

# x_index = [-40, -20, 0]
#
# for snake_index in range(3):
#     snake = Turtle(shape="square")
#     snake.color("white")
#     snake.goto(x=x_index[snake_index], y=0)

# 강의

starting_position = [(0, 0), (-20, 0), (-40, 0)] # 튜플로 설정

segments = []

for position in starting_position:
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.goto(position)
    segments.append(snake)


game_is_on = True
while game_is_on:
    screen.update() # tracer 메소드와 짝 / 최종 그림을 화면에 한 번에 업데이트
    time.sleep(0.1)

    # 마지막 segment 조각이 바로 앞 조각 위치로 차례대로 하나씩 이동하는 원리
    for seg_num in range(len(segments) - 1, 0, -1 ): # range(start=2, stop=0, step=-1) -> range 함수는 c 언어에서 가져온것이기에 인자 값에 키워드를 넣으면 에러가 뜬다.
        new_x = segments[seg_num - 1].xcor() # 마지막 seg가 바로 앞 seg 위치로 이동하니깐 -1 해줌
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y) # 마지막 seg 가 바로 앞 seg 위치로 이동

    segments[0].forward(20)













screen.exitonclick()