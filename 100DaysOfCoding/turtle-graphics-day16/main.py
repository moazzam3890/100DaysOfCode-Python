# from turtle import Turtle, Screen
#
# champu = Turtle()
#
# champu.shape("turtle")
#
# champu.color("DarkOrange", "brown")
# champu.position()
# champu.fd(100)
# champu.setheading(75)
# champu.fd(50)
#
#
# turtle_screen = Screen()
# turtle_screen.exitonclick()
# turtle_screen.title("Welcome to Turtle Cage.")

from prettytable import PrettyTable
table_object = PrettyTable()
table_object.add_column("Pokemon Name",
                        ["Pikachu", "Squirtle", "Charmandor"])
table_object.add_column("Type",
                        ["Electric", "Water", "Fire"])
table_object.align = "l"
print(table_object)


table_object.clear()


table_object.field_names = ["Serial Number", "Pokemon Name", "Type"]
table_object.add_rows(
    [
        ["#001", "Pikachu", "Electric"],
        ["#002", "Squirtle", "Water"],
        ["#003", "Charmandor", "Fire"],
    ]
)
table_object.align["Serial Number"] = "l"

print(table_object)


