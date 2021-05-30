# # Try these line of code:
# try:
#     file = open("a_file.txt")
#     dictionary = {"key": "value"}
#     print(dictionary["keey"])
# # Catching the exceptions that if error occurs above then execute this line of code:
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesnt exist")
#
# except IndexError:
#
# # Execute this line of code if there was no error:
# else:
#     content = file.read()
#     print(content)
# # Execute this no matter what:
# finally:
#     # file.close()
#     # print("File closed")
#     raise TypeError("This is self made.")
#


fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)





