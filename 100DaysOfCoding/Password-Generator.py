#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
rand_letter = 0
rand_symbol = 0
rand_number = 0
saved_password = []
for l in range(0, (nr_letters)):
  rand_index_letter = random.randint(0, (len(letters)-1))
  # print(rand_index_letter)
  rand_letter = letters[rand_index_letter]
  print(rand_letter, end = "")
  saved_password.append(rand_letter)

for s in range(0, nr_symbols):
  rand_index_symbol = random.randint(0, (len(symbols)-1))
  rand_symbol = symbols[rand_index_symbol]
  print(rand_symbol, end = "")
  saved_password.append(rand_symbol)

for n in range(0, nr_numbers):
  rand_index_number = random.randint(0, (len(numbers)-1))
  rand_number = numbers[rand_index_number]
  print(rand_number, end="")
  saved_password.append(rand_number)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print("\n\n\n")

combined_list = [letters, numbers, symbols]
# print(saved_password+"\n")
for hard in range(0, len(saved_password)):
    random_hard_index = random.randint(0, (len(saved_password)-1))
    rand_hard_number = saved_password[random_hard_index]
    print(rand_hard_number, end="")



