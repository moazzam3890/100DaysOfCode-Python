import random

# Pictures of ROCK, PAPER and SCISSORS.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]
random_selection = random.randint(0, 2)
user_selection = int(input("Please type '0' for rock, '1' for paper and '2' for scissors: "))
if user_selection > 2:
    print("You've typed an invalid number. You lose!")
elif random_selection == 2 and user_selection == 0:
    print(f"Computer Selected Scissors!\n{list[random_selection]}\n")
    print(f"You've Selected Rock!\n{list[user_selection]}\n")
    print("You Won! Hurraaaah!")
elif random_selection == 1 and user_selection == 0:
    print(f"Computer Selected Paper!\n{list[random_selection]}\n")
    print(f"You've Selected Rock!\n{list[user_selection]}\n")
    print("Computer Win! Good luck next time..")
elif random_selection == 0 and user_selection == 1:
    print(f"Computer Selected Rock!\n{list[random_selection]}\n")
    print(f"You've Selected Paper!\n{list[user_selection]}\n")
    print("You Won! Hurraaaah!")
elif random_selection == 2 and user_selection == 1:
    print(f"Computer Selected Scissors!\n{list[random_selection]}\n")
    print(f"You've Selected Paper!\n{list[user_selection]}\n")
    print("Computer Win! Good luck next time..")
elif random_selection == 0 and user_selection == 2:
    print(f"Computer Selected Rock!\n{list[random_selection]}\n")
    print(f"You've Selected Scissors!\n{list[user_selection]}\n")
    print("Computer Win! Good luck next time..")
elif random_selection == 1 and user_selection == 2:
    print(f"Computer Selected Paper!\n{list[random_selection]}\n")
    print(f"You've Selected Scissors!\n{list[user_selection]}\n")
    print("You Won! Hurraaaah!")
else:
    print(f"Computer Choose: {list[random_selection]}\nYou Choose: {list[user_selection]}\nDraw!")

