# Mile to Km Converter Project.
# 1 mile = 1.60934 km

from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def converter():
    print("converter")
    con = float(input.get())
    label3.config(text=round(con * 1.60934))


# Label
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)


# Button
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)




window.mainloop()