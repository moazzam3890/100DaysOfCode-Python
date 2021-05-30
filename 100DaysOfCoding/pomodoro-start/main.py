from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
REPS = 0
timer = None
pause = None


# # ---------------------------- Pause Button Mechanism ------------------------------- #
# def resume_button():
#     window.after_idle(pause, 1000, pause_button, timer)
#
#
# def pause_button():
#     global pause
#     pause = window.after_cancel(timer)

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    REPS = 0
    timer_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_start():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global REPS
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks += "✅"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=30, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=timer_start)
start_button.grid(column=0, row=2)

# pause_button = Button(text="Pause", highlightthickness=0, command=pause_button)
# pause_button.grid(column=1, row=2)
#
# resume_button = Button(text="Resume", highlightthickness=0, command=resume_button)
# resume_button.grid(column=1, row=4)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=RED, bg=YELLOW)
check_mark.grid(column=1, row=3)

canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()
