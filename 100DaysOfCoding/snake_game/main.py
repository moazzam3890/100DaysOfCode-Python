from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# Screen Setup:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating a Snake with square turtles:
snake = Snake()
food = Food()
score = Score()
# Controlling snake on screen:
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #     Detect Collision with food:
    if snake.all_snake_parts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment()

    #     Detect Collision with the wall:
    if snake.all_snake_parts[0].xcor() > 280 or snake.all_snake_parts[0].xcor() < -280 or snake.all_snake_parts[
        0].ycor() > 280 or snake.all_snake_parts[0].ycor() < -280:
        score.reset()
        snake.reset()

#     Detect Collision with tail:
    for part in snake.all_snake_parts[1:]:
        if snake.all_snake_parts[0].distance(part) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
