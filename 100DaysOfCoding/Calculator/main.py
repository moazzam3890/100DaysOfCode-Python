# Calculator:

from art import logo

# Addition
def add(n1,n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

# Operations of Calculator:
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("Please enter a number: "))

    for symbols in operations:
        print(symbols)

    continuity_check = True
    while continuity_check:
            
        operation_to_perform = input("Please select an operation: ")

        num2 = float(input("Please enter next number: "))

        call_to_operation = operations[operation_to_perform]
        answer = call_to_operation(num1, num2)

        print(f"{num1} {operation_to_perform} {num2} = {answer}")

        asking_to_continue = input(f"Press 'y' to continue operations with {answer} and 'n' to start a new calculation: ")

        if asking_to_continue == "n":
            calculator()
        
        elif asking_to_continue == "y":
            num1 = answer
calculator()