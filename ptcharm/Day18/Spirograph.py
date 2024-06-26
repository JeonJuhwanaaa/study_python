# Make a Spirograph

import turtle
from turtle import Turtle,Screen
import random

# 혼자 한 것.

tur = Turtle()
tur.speed("fastest")
# tur.pensize(10)
turtle.colormode(255)

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

direction = 5

for _ in range(100):
    tur.color(random_colors())
    tur.circle(200)
    tur.setheading(direction)
    direction += 5

# ---------------------------------------

# 강의에서 한 것.
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tur.color(random_colors())
        tur.circle(100)
        current_heading = tur.heading() # 기본 머리 방향은 0.0
        tur.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()