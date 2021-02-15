from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

score = Score()
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.right_go_up, "Up")
screen.onkey(r_paddle.right_go_down, "Down")
screen.onkey(l_paddle.left_go_up, "w")
screen.onkey(l_paddle.left_go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     Detect Collision with the Upper and Lower Walls:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

#     Detect Collision with the paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

#     Detection of miss:
    if ball.distance(r_paddle) > 50 and ball.xcor() > 390:
        ball.paddle_misses()
        score.l_point()
        score.update()

    if ball.distance(l_paddle) > 50 and ball.xcor() < -390:
        ball.paddle_misses()
        score.r_point()
        score.update()


screen.exitonclick()


