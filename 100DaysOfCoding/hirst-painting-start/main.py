# Code to import colors from image with the help of colorgram package.
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)

import turtle as t
import random

pinky = t.Turtle()
pinky.speed(3)
pinky.shape("circle")
pinky.width(20)
pinky.penup()
pinky.hideturtle()
t.colormode(255)

rgb_colors = [(202, 164, 109), (238, 240, 245),
              (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19)]


position = [-200, -200]


def dot_positions():
    pinky.penup()
    pinky.setpos(position[0], position[1])
    position[1] += 50


def movement():
    for _ in range(10):
        random_color = random.choice(rgb_colors)
        pinky.dot(20, random_color)
        pinky.fd(50)


count = 0
while not count == 10:
    dot_positions()
    movement()
    count += 1


screen = t.Screen()
screen.exitonclick()


