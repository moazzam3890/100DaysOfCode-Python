import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle = Player()
screen.listen()
screen.onkey(turtle.move, "Up")
car = CarManager()
score = Scoreboard()

game_over = False
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.move_car()
    car.init_car()
    if turtle.ycor() > 280:
        turtle.init_turtle()
        score.update_scoreboard()
        car.speed_increment()

    for c in car.car_list:
        if turtle.distance(c) < 20:
            game_over = True
            while game_over:
                score.game_over()

    screen.update()
