import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S. States Game")

# 이미지 로드해서 shape 으로 만들기.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# ---------------------------------------------------------------
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# # 이벤트 리스너 - 마우스가 클릭되는 것을 보고 있다가 () 안 함수 호출.
# # 즉, 여기선 x, y 좌표를 전달한다.
# turtle.onscreenclick(get_mouse_click_coor)
# ---------------------------------------------------------------

us_state = pandas.read_csv("50_states.csv")
all_states = us_state.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    # title() 함수를 사용하면 전부 대문자, 소문자로 입력받아도 첫 알파벳만 대문자로 출력 -> ex) OHIO --> Ohio
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states Correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":

        # 정답을 놓친 것들을 따로 모아서 csv 파일로 만들기.
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = us_state[us_state.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# screen.mainloop() # 클릭해도 화면이 사라지지않고 유지.
screen.exitonclick()
