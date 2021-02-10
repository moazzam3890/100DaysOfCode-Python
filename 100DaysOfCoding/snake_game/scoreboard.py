from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
COLOR = "white"
POSITION = (0, 270)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER.", move=False, align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.update_score()
