from turtle import Turtle
MOVE_DISTANCE = 20
COLOR = "green"
SHAPE = "square"


class Snake:
    """Create a snake object with default shape, color, starting position, parts object."""

    def __init__(self):
        self.shape = SHAPE
        self.color = COLOR
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.all_snake_parts = []
        self.body_parts_creation()

    def body_parts_creation(self):
        for position in self.positions:
            self.add_parts(position)

    def add_parts(self, position):
        new_snake_part = Turtle(self.shape)
        new_snake_part.color(self.color)
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.all_snake_parts.append(new_snake_part)

    def extend(self):
        self.add_parts(self.all_snake_parts[-1].position())

    def move(self):
        for part in range(len(self.all_snake_parts) - 1, 0, -1):
            new_x = self.all_snake_parts[part - 1].xcor()
            new_y = self.all_snake_parts[part - 1].ycor()
            self.all_snake_parts[part].goto(new_x, new_y)
        self.all_snake_parts[0].fd(MOVE_DISTANCE)

    def change_attr(self, shape, color):
        self.shape = shape
        self.color = color

    def up(self):
        if self.all_snake_parts[0].heading() != 270:
            self.all_snake_parts[0].setheading(90)

    def down(self):
        if self.all_snake_parts[0].heading() != 90:
            self.all_snake_parts[0].setheading(270)

    def left(self):
        if self.all_snake_parts[0].heading() != 0:
            self.all_snake_parts[0].setheading(180)

    def right(self):
        if self.all_snake_parts[0].heading() != 180:
            self.all_snake_parts[0].setheading(0)
