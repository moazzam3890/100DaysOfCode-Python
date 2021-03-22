import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=600, height=450)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "italic"))
my_label.pack(side="left", ipadx=25)

window.mainloop()
