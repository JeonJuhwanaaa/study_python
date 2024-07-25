import another_module
print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle() # 다른 클래스를 불러와 객체를 만드는 방법
print(timmy)

# 속성에 접근하는 법 / 호출
timmy.shape("turtle") # 점 포인트 모양을 .shape 메소드 사용하여 거북이 포인트 모양으로 변형
timmy.color("coral") # 포인트 모양의 .color 메소드로 색을 변경
timmy.forward(100) # 거북이모양 포인트가 100 거리 이동

my_screen = Screen() # 새로운 창 띄우기
print(my_screen.canvheight) # screen의 높이
my_screen.exitonclick() # 마우스 클릭의 효과가 감지되야지만 종료되게 설정


# ---------------------------------------------------------------------------------------

from prettytable import PrettyTable

table = PrettyTable() # 표 만들기 틀 호출

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"]) # 하나의 컬럼에 속성 값 넣기
table.add_column("Type",["Electric", "Water", "Fire"]) # 또 하나의 컬럼에 속성 값 설정

table.align = "r" # table 의 정렬 방향 설정 / l - 왼쪽, c - 중앙, r - 오른쪽

print(table)
