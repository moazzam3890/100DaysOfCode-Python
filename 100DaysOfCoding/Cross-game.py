# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# if position == "11":
#   row1.pop(0)
#   row1.insert(0, "X")
# elif position == "12":
#   row2.pop(0)
#   row2.insert(0, "X")
# elif position =="13":
#   row3.pop(0)
#   row3.insert(0, "X")
# elif position == "21":
#   row1.pop(1)
#   row1.insert(1, "X")
# elif position == "22":
#   row2.pop(1)
#   row2.insert(1, "X")
# elif position == "23":
#   row3.pop(1)
#   row3.insert(1, "X")
# elif position == "31":
#   row1.pop(2)
#   row1.insert(2, "X")
# elif position == "32":
#   row2.pop(2)
#   row2.insert(2, "X")
# elif position == "33":
#   row3.pop(2)
#   row3.insert(2, "X")
# else:
#   print("Please enter a valid number")

colomn = int(position[0])-1
row = int(position[1])-1


map[row][colomn] = "X"





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")