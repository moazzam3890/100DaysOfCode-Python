from turtle import Turtle
import random
SHAPE = "circle"
COLOR = "yellow"
POSITION_X = 0
POSITION_Y = 270
F_WIDTH = 0.5
F_LENGTH = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_wid=F_WIDTH, stretch_len=F_LENGTH)
        self.color(COLOR)
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(POSITION_X, POSITION_Y)
        random_y = random.randint(POSITION_X, POSITION_Y)
        self.goto(random_x, random_y)
