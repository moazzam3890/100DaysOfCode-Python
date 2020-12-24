
from caeser_cypher_art import logo
print(logo)

from caeser_cypher_functions import caeser
ask_for_retry = True

while ask_for_retry:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caeser(text_input=text,shifting=shift,direction_check=direction)

    asking = input("Type 'yes' to start again and 'no' to end.").lower()
    if asking == "no":
        ask_for_retry = False
        print("Goodbye")