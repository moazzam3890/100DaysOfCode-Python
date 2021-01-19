from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

turn_off = False
while not turn_off:
    user_selection = input(f"What would you like to have? {m.get_items()}:")

    if user_selection == "off":
        print("Machine is turning OFF. BYE BYE...")
        turn_off = True
    elif user_selection == "report":
        cm.report()
        mm.report()
    else:
        item = m.find_drink(user_selection)
        if item is None:
            print("We have only three options available.")
        can_make = cm.is_resource_sufficient(item)
        if can_make is True:
            mm.make_payment(item.cost)
            cm.make_coffee(item)



