from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine();

def run():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        exit()
    elif choice == "report":
        coffee_maker.report()
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
            run()
    else:
        run()


run()