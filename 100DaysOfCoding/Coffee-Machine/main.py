MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def report():
    """Generate a report when called."""
    for key in resources:
        if key == "coffee":
            print(f"{key}:{resources[key]}g")
        else:
            print(f"{key}:{resources[key]}ml")
    print(f"Money: ${profit}")


def coin_total(quarters_in, dimes_in, nickles_in, pennies_in):
    """Returns the total of inserted coins."""
    return (0.25 * quarters_in) + (0.1 * dimes_in) + (0.05 * nickles_in) + (0.01 * pennies_in)


def check_resources(coffee):
    """Returns True if the resources are sufficient in machine and False if resources are not sufficient."""
    if coffee == "espresso":
        if resources["water"] < 50:
            print("Sorry there is not enough water.")
            return False
        elif resources["coffee"] < 18:
            print("Sorry there is not enough Coffee.")
            return False
        else:
            return True
    elif coffee == "latte":
        if resources["water"] < 200:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] < 150:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] < 24:
            print("Sorry there is not enough Coffee.")
            return False
        else:
            return True
    elif coffee == "cappuccino":
        if resources["water"] < 250:
            print("Sorry there is not enough water.")
            return False
        elif resources["milk"] < 100:
            print("Sorry there is not enough milk.")
            return False
        elif resources["coffee"] < 24:
            print("Sorry there is not enough Coffee.")
            return False
        else:
            return True


def compare_cost(user_choice, monetary_value_in):
    """Returns True if the inserted coins are enough to buy coffee and False if the inserted coins are not enough."""
    if monetary_value_in < MENU[user_choice]["cost"]:
        return False
    else:
        return True


def transaction(user_input):
    """Returns the monetary Value. 0 if the resources are not enough."""
    # TODO: 4. check the resources sufficient for the asked product.
    # TODO: 4.1. check all three resources i.e. water, milk and coffee.
    # TODO: 4.2. print the message of unavailability of each resource separately.
    continuity = check_resources(user_input)
    if continuity:
        # TODO: 5. Process Coins.
        print("Please insert Coins.")
        # TODO: 5.2. Check inserted coins and store its values. Quarter = $0.25, Dimes = $0.10, nickles = $0.05, pennies = $0.01
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        # TODO: 5.3. Calculate the total value by multiplying the inserted coins with each coin value and adding all of them.
        monetary_value = coin_total(quarters, dimes, nickles, pennies)
        return monetary_value
    elif not continuity:
        return 0


def return_money():
    """Returns the amount that returned to the machine user with roundup to two decimal places."""
    return_amount = monetary_value_main - MENU[ask_user]["cost"]
    return round(return_amount, 2)


def deduct_resources(user_input):
    """Deduct the resources from the resources dictionary."""
    if user_input == "espresso":
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
    else:
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]


# TODO: 1.2. Repeat asking everytime once the drink is dispensed.
check_for_off = False


while not check_for_off:

    # TODO: 1. Ask user for the options available.
    ask_user = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 2. check for 'off' string if inserted then turn of the machine.
    if ask_user == "off":

        check_for_off = True
    # TODO: 3. Print report of the resources available in machine.
    elif ask_user == "report":
        report()
    # TODO: 1.1. Check the user input to decide what to do next.
    elif ask_user == "espresso" or ask_user == "latte" or ask_user == "cappuccino":

        monetary_value_main = transaction(ask_user)
        if monetary_value_main != 0:


            # TODO: 6. Check for the transaction.
            # TODO: 6.1. Compare the total value of the inserted coins with the coffee value and make a decision.
            decision = compare_cost(ask_user, monetary_value_main)

            # TODO: 6.2. if user inserted enough money then add the cost of drink must be added in machine as a profit.
            if decision:

                profit += MENU[ask_user]["cost"]
                # TODO: 7.1. If transaction was successful and resources are sufficient then deduct the resources available before making.
                deduct_resources(ask_user)
            else:
                print("Sorry that's not enough Money. Money refunded")

                # TODO: 6.3. If user has inserted extra money then it should be calculated and returned.
            print(f"Here is ${return_money()} dollars in change.")
            # TODO: 7. Make Coffee.
            print(f"Here is your {ask_user} ☕. Enjoy!")










