from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()
coffee_maker.report()

# print(menu.get_items())

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



# -- Program Requirements --

# 1. Print report.
# 2. Check resources sufficient?
# 3. Process coins.
# 4. Check transaction successful?
# 5. Make Coffee.