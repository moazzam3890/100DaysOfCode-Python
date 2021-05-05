from tkinter import *


def calculation():
    miles = float(user_input.get())
    km = miles * 1.609
    label_4.config(text=km)


window = Tk()
window.title("Miles to Kilo Meter Converter")
window.minsize(width=100, height=100)

# User Input:
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# button:
button = Button(text="Calculate", activebackground="blue", command=calculation)
button.grid(column=1, row=2)

# label 1
label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

# label 2
label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)

# label 3
label_3 = Label(text="KM")
label_3.grid(column=2, row=1)

# label 4
label_4 = Label(text="0")
label_4.grid(column=1, row=1)

window.mainloop()
