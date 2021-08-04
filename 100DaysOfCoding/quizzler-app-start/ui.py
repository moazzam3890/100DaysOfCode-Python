from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz GUI")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", highlightthickness=0, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.Canvas = Canvas(height=250, width=300)
        self.question_text = self.Canvas.create_text(
            150,
            125,
            width=280,
            text="Chai Pi lo",
            font=["Arial", 20, "italic"]
        )
        self.Canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_button = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_button, highlightthickness=0, command=self.right_answer)
        self.right_button.grid(row=2, column=1)

        wrong_button = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_button, highlightthickness=0, command=self.wrong_answer)
        self.wrong_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.Canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.Canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.Canvas.itemconfig(self.question_text, text="You've completed the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_answer(self):
        self.feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, answer):
        if answer:
            self.Canvas.config(bg="Green")
        else:
            self.Canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)


