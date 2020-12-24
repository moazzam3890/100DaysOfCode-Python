from caeser_cypher_art import alphabet

def caeser(text_input, shifting, direction_check):
    end_result = ""
    if direction_check == "decode":
        shifting *= -1
    for letter in text_input:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shifting
            end_result += alphabet[new_position]
        else:
            end_result += letter
    print(f"The {direction_check}d text is {end_result}")