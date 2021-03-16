import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)
name_turtle = turtle.Turtle()
name_turtle.hideturtle()
name_turtle.penup()
states_data = pandas.read_csv("50_states.csv")
states_in_list = states_data["state"].to_list()


count = 0
game_continue = True
guessed_states = []

while game_continue:
    user_guess = screen.textinput(title=f"{count}/50 Guess the States", prompt="What's your guess?").title()
    count += 1
    s_no = -1
    if user_guess == "Exit":
        states_to_learn = [state for state in states_in_list if state not in guessed_states]
        break
    for state in states_in_list:
        s_no += 1
        if user_guess == state:
            guessed_states.append(state)
            state_row = states_data[states_data.state == state]
            state_row_dict = state_row.to_dict()
            # print(state_row_dict["x"])
            name_turtle.goto(int(state_row.x), int(state_row.y))
            name_turtle.write(state, align="center")
        if count == 50:
            game_continue = False


dataframe = pandas.DataFrame(states_to_learn)
dataframe.to_csv("states_to_learn.csv")
