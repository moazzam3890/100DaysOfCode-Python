from art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []

ask = input("Do you wanna play Black-Jack: type 'y' for Yes and 'n' for no. ")
if ask == "y":
    restart = True

    while restart:
        print (logo)
        
        def pick_cards():
            for _ in range(2):
                random_card = random.choice(cards)
                user_cards.append(random_card)
                comp_random_card = random.choice(cards)
                computer_cards.append(comp_random_card)

        def cards_dealing():
            
            for card in user_cards:
                user_score += card

            for card in computer_cards:
                computer_score += card

            if user_score == 21:
                print("You've got a BLACK-JACK. You Win.")
            elif computer_score == 21:
                print("Computer got a BLACK-JACK. You Lose.")
        
        pick_cards()
        cards_dealing()
        user_score = 0
        computer_score = 0
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first Cards: {computer_cards[0]}")

        user_decision = input("Type 'y' to get another card, type 'n' to pass: ")

        play_again = input("Do you want to play a game of Balck-Jack? Type 'y' or 'n': ")
        if play_again == 'n':
            restart = False