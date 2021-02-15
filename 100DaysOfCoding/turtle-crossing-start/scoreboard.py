from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.init_level()

    def init_level(self):
        self.goto(-210, 260)
        self.write(f"LEVEL : {self.level}", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.increment_level()
        self.write(f"LEVEL : {self.level}", align="center", font=FONT)

    def increment_level(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)
