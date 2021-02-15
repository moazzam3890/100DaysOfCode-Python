from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.init_car()

    def init_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-240, 240)
            new_car.goto(300, random_y)
            new_car.setheading(180)
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.fd(self.speed)

    def speed_increment(self):
        self.speed += MOVE_INCREMENT
