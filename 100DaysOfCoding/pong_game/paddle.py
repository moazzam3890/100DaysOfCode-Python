from turtle import Turtle
LOCATION = ()


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.create_paddle(location)

    def create_paddle(self, position):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def right_go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def right_go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)

    def left_go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def left_go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
