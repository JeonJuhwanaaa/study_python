# from turtle import Turtle, Screen
#
# turtle = Turtle()
# turtle.shape("turtle")
#
# screen = Screen()
#
#
# def move_forwards():
#     turtle.forward(10)
#
# screen.listen() # 키보드의 특정 키를 누르면 촉발되는 함수. 바인딩 필요!
# # 키 누르기를 코드 안의 이벤트에 바인딩하려면 이벤트 리스터를 사용헤야한다. -> onkey 메소드
# # space 키를 눌러 move_forward 함수가 실행 됨.
# # 중요한 것 -> 함수를 인수로 사용할 땐 끝에 () 괄호 사용 안한다!
# # 괄호를 넣으면 그 자리에서 실행이 되기 때문이다.
# # 우리가 원하는 것은 onkey 메소드가 스페이스 바가 눌리는 이벤트를 듣고 실행이 되야한다.
#
# screen.onkey(key="space", fun=move_forwards) # .onkey() 메소드가 가 고차함수
# screen.exitonclick() # 화면이 바로 사라지지 않게 한다.

# 고차함수란, 다른 함수와 함께 작동하는 함수.

# ---------------------------------------------------------------------

# 에치어 스케치 만들기

# W = Forwards / S = Backwards / A = Counter-Clockwise / D = Clockwise / C = Clear drawing

from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()

def w():
    turtle.forward(10)

def s():
    turtle.backward(10)

def a():
    heading = turtle.heading() + 10
    turtle.setheading(heading)

def d():
    heading = turtle.heading() - 10
    turtle.setheading(heading)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.onkey(key="w", fun=w)
screen.onkey(key="s", fun=s)
screen.onkey(key="a", fun=a)
screen.onkey(key="d", fun=d)
screen.onkey(key="c", fun=clear)

screen.listen()
screen.exitonclick()

# ---------------------------------------------------------------------