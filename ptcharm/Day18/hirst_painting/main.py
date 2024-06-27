# Cologram 을 이용해서 image 안에 있는 컬러들 튜플로 뽑아보기
# colorgram 공식 문서 사이트 -> https://pypi.org/project/colorgram.py/
# 터미널 켜서 pip install colorgram.py 작성 하면 설치 완료!

# import colorgram
#
# # Extract 6 colors from an image.
# # 같은 무조건 폴더 안에 있는 이미지 여야한다.
# # 이미지아 엤는 컬러 추출 함수 .extract()
# colors = colorgram.extract("image.jpg",30)
# print(colors)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b) # 튜플로 전환
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(245, 158, 50), (49, 81, 168), (62, 37, 50), (234, 63, 109), (171, 19, 62), (249, 211, 29), (156, 187, 4), (89, 168, 212), (235, 126, 167), (249, 85, 41), (6, 169, 203), (3, 98, 83), (34, 57, 136), (249, 210, 0), (187, 41, 69), (241, 156, 186), (57, 36, 34), (3, 72, 59), (191, 79, 41), (63, 119, 110), (239, 168, 156), (20, 35, 90), (134, 171, 164), (115, 106, 173), (144, 213, 225), (121, 39, 38)]

# --------------------------------------------------------

# 1번째 시도

# from turtle import Turtle, Screen
# import random

# tur = Turtle()
# # tur.shape("turtle")
# tur.pensize(20)
#
# def draw_shape(move):
#     for _ in range(move):
#         tur.color((245, 158, 50))
#         tur.forward(1)
#         tur.penup()
#         tur.forward(50)
#         tur.pendown()
#
# up = 50
#
# for _ in range(5):
#     draw_shape(5)
#     tur.penup()
#     tur.home()
#     tur.sety(up)
#     tur.penup()
#     up += 50
#
# -----------------------------------------------

# 2번째 시도

# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
#
# def move():
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)
#
# num = 10
# for _ in range(10):
#     tim.setheading(255 - num)
#     tim.forward(250 - num)
#     tim.setheading(0)
#     move()
#     tim.home()
#     num += 10

# -----------------------------------------------

# 최종 결과

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
