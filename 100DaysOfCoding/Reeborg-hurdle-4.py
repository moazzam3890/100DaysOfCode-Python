def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if not front_is_clear() and not right_is_clear():
        turn_left()
    if front_is_clear() and not right_is_clear():
        move()
    else:
        jump()