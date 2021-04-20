# import tkinter
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=600, height=450)

# Label

my_label = Label(text="I am a Label", font=("Arial", 20, "italic"))
my_label.pack(side="left", ipadx=100)

# Procedure to change the property:

# my_label.config(text="New Text")
my_label["text"] = "New Text"


def button_clicked():
    enter = user_input.get()
    my_label.config(text=enter)


# Button:
button = Button(text="Click Me", command=button_clicked, background="red", activebackground="blue")
button.pack()


# Input
user_input = Entry(width=10)
user_input.pack()


window.mainloop()
