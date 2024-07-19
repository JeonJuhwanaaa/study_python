from tkinter import *

THEME_COLOR = "#375362"
WHITE = "#FEFBF6"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        canvas = Canvas(width=300, height=250)
        canvas.create_text(150, 125, text="quiz", font=("Arial", 20, "italic"))
        canvas.grid(column=0, row=1, columnspan=2)

        label = Label(padx=20, pady=20, text="Score: 0", bg=THEME_COLOR, fg=WHITE)
        label.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        true_button = Button(image=true_img, highlightthickness=0)
        true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        false_button = Button(image=false_img, highlightthickness=0)
        false_button.grid(column=1, row=2)



        self.window.mainloop()
