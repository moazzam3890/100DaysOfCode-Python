from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYERS = []


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.players = []
        self.init_turtle(position)

    def init_turtle(self, position):
        # new_player = Turtle()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(position)

    def move(self):
        self.fd(MOVE_DISTANCE)
