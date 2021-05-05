# import tkinter
from tkinter import *


def button_clicked():
    enter = user_input.get()
    my_label.config(text=enter)


def second_button():
    status = new_button.get()
    print(status)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=600, height=450)

# Label
my_label = Label(text="I am a Label", font=("Arial", 20, "italic"))
my_label.grid(column=0, row=0)
# my_label.config(text="New Text")
my_label["text"] = "New Text"

# Button:
button = Button(text="Click Me", command=button_clicked, background="red", activebackground="blue")
button.grid(column=1, row=1)

# Second Button:
new_button = Button(text="Click Me Please", activebackground="yellow")
new_button.grid(column=2, row=0)

# Input
user_input = Entry(width=10)
user_input.grid(column=3, row=3)

window.mainloop()
