from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()

# 화면 타이틀 설정.
window.title("My First GUI Program")
# 화면 크기 설정.
window.minsize(width=500, height=300)

# padding 값 설정.
window.config(padx=100, pady=200)

# -------------------------------------------------------------------------

# << pack() 메소드 >> --> 디폴트 값은 항상 위에서 부터 배치되고 다른 위젯은 이전 것의 바로 아래에 배치.
# 매개변수로 side -> 원하는 위치 설정/ expand -> 화면 가득 차지 / 등 있다.
# pack의 문제는 위치를 정확하게 명시하기 어렵다.

# << place() 메소드 >> --> 어떤 위젯의 위치를 설정할 때 x, y 값으로 정확한 위치 선정 가능.
# 단점: 너무 구체적이라 위치 선정 시 계산적으로 해야한다.

# << grid() 메소드 >> --> 열과 행으로 나눠서 위치 선정.

# ※ 주의 : grid 와 pack 은 같이 사용 불가!

# -------------------------------------------------------------------------

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# 위젯 위치 설정.
my_label.grid(column=0, row=0)
# padding 값 설정.
my_label.config(padx=50, pady=0)


#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


# 화면이 보여지게 유지해줌.
window.mainloop()