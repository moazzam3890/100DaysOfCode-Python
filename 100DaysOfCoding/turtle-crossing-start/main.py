import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SINGLE_PLAYER = (0, -280)
PLAYER_1 = (150, -280)
PLAYER_2 = (-150, -280)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


turtle1 = Player(PLAYER_1)
turtle2 = Player(PLAYER_2)
screen.listen()
screen.onkey(turtle1.move, "Up")
screen.onkey(turtle2.move, "w")
car = CarManager()
score = Scoreboard()

game_over = False
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.move_car()
    car.init_car()
    # Detect if player cross successfully:
    if turtle1.ycor() > 280:
        turtle1.init_turtle(PLAYER_1)
        score.update_scoreboard()
        car.speed_increment()
    # Detect the collision:
    for c in car.car_list:
        if turtle1.distance(c) < 20:
            game_over = True
            while game_over:
                score.game_over(1)

    if turtle2.ycor() > 280:
        turtle2.init_turtle(PLAYER_2)
        score.update_scoreboard()
        car.speed_increment()
    # Detect the collision:
    for c in car.car_list:
        if turtle2.distance(c) < 20:
            game_over = True
            while game_over:
                score.game_over(2)

    screen.update()
