from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.l_score_write()
        self.goto(100, 200)
        self.r_score_write()

    def l_score_write(self):
        self.write(self.l_score, align="center", font=("arial", 70, "normal"))

    def r_score_write(self):
        self.write(self.r_score, align="center", font=("arial", 70, "normal"))

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1