from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

try_again = 'y'

while try_again == 'y':
    user_choice = int(input("\nWelcome\nWhat would you like to do today?\n1. Have a drink\n2. Fetch Machine Report\n3. Exit\n"))
    if user_choice == 1:
        drink_choice = input("What drink would you like?\n" + menu.get_items() + "\n").lower()
        drink = menu.find_drink(drink_choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        try_again = input("\nTry again?\nY or N\n").lower()
    elif user_choice == 2:
        print(coffee_maker.report())
        print(money_machine.report())
    elif user_choice == 3:
        exit()
    try_again = input("\nTry again?\nY or N\n").lower()
