from tkinter import *
from tkinter import messagebox # 팝업 창.
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter = [choice(letters) for _ in range(randint(8, 10))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]
    number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter + symbol + number
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    # 위 코드를 아래 코드로 간소화
    password = "".join(password_list)
    # print(f"Your password is: {password}")

    password_write.delete(0,END)
    password_write.insert(0, password)

    # pyperclip - 자동으로 복사 기능.
    # 즉, generate_password 버튼을 누르면 생성 즉시 자동 복사된 상태라서
    # 다른 곳에 Cntr+V 해주기면 하면 붙여넣기 가능.
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# << Challenge >>
# 1. Create a function called save().
# 2. Write to the data inside the entries to data. txt file when the Add button is clicked.
# 3. Each website, email, and password combination should be on a new line inside the file.
# 4. All fields need to be cleared after Add button is pressed.

def save():
    website = website_write.get()
    email = name_write.get()
    password = password_write.get()

    # 빈 칸 확인
    # if len(website) == 0 or len(password) == 0:
    if website == "" or password == "":
        messagebox.showinfo(title="Worning", message="입력하지 않은 정보가 있습니다.\n빈 칸을 채워주세요.")
    else:
        # 팝업 알람 창.
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                               f"\nPassword: {password} \nIs it ok to save?")

        # 알림 팝업 창에서 ok 클릭 시 파일에 정보 저장.
        if is_ok:
            # .txt 파일 만들기. / * mode: a(append), w(write), r(read)
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_write.delete(0, END)
                password_write.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
rock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=rock_img)
canvas.grid(column=1, row=0)

# ---------------------------- Label ------------------------------- #

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

name_label = Label(text="Email/Username:")
name_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# ---------------------------- Text Box(Entry) ------------------------------- #

website_write = Entry(width=35)
website_write.grid(column=1, row=1, columnspan=2)
website_write.focus()

name_write = Entry(width=35)
name_write.grid(column=1, row=2, columnspan=2)
name_write.insert(0, "1q2w3e4r@naver.com")

password_write = Entry(width=21)
password_write.grid(column=1, row=3)

# ---------------------------- Button ------------------------------- #

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3 )

add_button = Button(text="Add",width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()