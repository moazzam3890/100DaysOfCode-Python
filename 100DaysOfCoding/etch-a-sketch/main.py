from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    tim.right(5)


def anti_clockwise():
    tim.left(5)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(anti_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
