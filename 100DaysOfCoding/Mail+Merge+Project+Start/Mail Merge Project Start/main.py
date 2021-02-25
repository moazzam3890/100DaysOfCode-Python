#TODO: Create a letter using starting_letter.txt
# print(change_name)
with open("./Input/Names/invited_names.txt") as all_names:
    names = all_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_blueprint = letter.read()

#for each name in invited_names.txt
for name in names:
    stripped_name = name.strip()
    new_letter = letter_blueprint.replace("[name]", stripped_name)
    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as final_letter:
        final_letter.write(new_letter)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp