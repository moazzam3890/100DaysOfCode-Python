from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_input = screen.textinput(title="Make your bet", prompt="Select your turtle by entering color: ").lower()
color = ["red", "green", "blue", "yellow", "orange", "purple"]
y_position = [-200, -120, -40, 40, 120, 200]
all_turtles = []


for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_input:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_turtle_color = turtle.pencolor()
            if winning_turtle_color == user_input:
                print(f"You've Won! The {winning_turtle_color} turtle has won the race.")
            else:
                print(f"You've lost! The {winning_turtle_color} turtle has won the race.")

        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)


screen.exitonclick()
