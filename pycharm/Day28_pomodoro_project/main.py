from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
pause_state = False
pause_time = 0 # 일시정지 시 현재 타이머 시간 저장 용도.

# ---------------------------- TIMER RESET ------------------------------- #

def reset_button():
    global reps, pause_state, pause_time
    reps = 0
    pause_state = False
    pause_time = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    checkbox.config(text="")
    button1.config(text="Start", command=start_timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #

# << 🤞 Challenge !! >>
# Use the reps variable to count down the appropriate number of seconds.
# When you run the program the timer needs to switch between counting down
# the work time and the break time (tet with 1 minute rather than 25 minutes)

# # If it's the 1st/3rd/5th/7th/ rep:
# count_down(work_sec)
# # If it's the 8th rep:
# count_down(long_break_sec)
# # If it's 2nd/4th/6th rep:
# count_down(short_break_sec)

def pause_button():
    global pause_state, pause_time

    print(pause_time)

    if not pause_state:
        window.after_cancel(timer)
        button1.config(text="Resume", command=resume_timer)
        pause_state = True
    else:
        # count_down(pause_time)
        # button1.config(text="Pause", command=pause_button)
        # pause_state = False
        resume_timer()

def resume_timer():
    global pause_state

    print(type(pause_time))

    count_down(pause_time)

    button1.config(text="Pause", command=pause_button)
    pause_state = False

def start_timer():
    global reps, pause_state, pause_time

    if not pause_state:
        reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    button1.config(text="Pause", command=pause_button)

    if reps % 8 == 0:
        label.config(text="Break Time!", fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Break Time!", fg=PINK)
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        label.config(text="Work Time!", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# after(시간, 함수) 는 원하는 시간이 지나면 원하는 함수 실행시킨다.
def count_down(count):
    global timer, pause_state, pause_time

    # 245 / 60 = 4 minutes
    # 245 % 60 = 4분하고 남은 초
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0: # int
        count_sec = "00" # string
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        pause_time = count
        # if not pause_state: !!!!!!!!!!!!!!!!!!! 이놈 때문에 시간이 다시 흘러가지 않았던 것이다!!
        timer = window.after(1000, count_down, count - 1 )
    else:
        pause_state = False
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "🗸"

        checkbox.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# 화면에 padding 넣기.
window.config(padx=100, pady=50, bg=YELLOW)

# 화면에 이미지를 넣기.
# tomato.png 파일 크기 확인 후 넣을 것.
# highlightthickness=0 은 이미지 가장자리(테두리) 제거.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# create_image(x위치, y위치, image=) ※ image 에 그냥 파일명 쓰면 타입이 달라서 안된다.
# image 인자는 PhotoImage(file="파일 절대경로 또는 상대경로") 로 받아서 쓰기.
tomato_img = PhotoImage(file="tomato.png")
# 이미지가 캔버스 한가운데 있기를 원한다. 그럼 x 값을 폭의 절반으로 넣고
# y 값을 높이의 절반으로 넣을 수 있다.
canvas.create_image(100, 112, image=tomato_img)
# text 넣는 것도 x위치, y위치 필요.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack() # 화면 가운데로 가져오기.
canvas.grid(column=3, row=3)

label = Label()
label.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=3, row=2)

button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(column=2, row=4)

button2 = Button(text="Reset", highlightthickness=0, command=reset_button)
button2.grid(column=4, row=4)

checkbox = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkbox.grid(column=3, row=5)



window.mainloop()

##  문제가 발생..
# Resume button 을 눌러도 시간이 이어서 흘러가지가 않는다..
# 뭐가 문제일까..

# after_cancel() 함수가 걸렸기 때문인가??