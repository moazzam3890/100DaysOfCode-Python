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
        self.high_score = 0
        self.update_high_score()
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(POSITION)
        self.update_score()

    def update_high_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_score()
        self.update_high_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER.", move=False, align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        self.update_score()
