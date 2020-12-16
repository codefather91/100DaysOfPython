#Coffee Machine program
# Implement the working of a coffee machine

# Initialise the machine

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

machine_balance = 0.0
user_money = 0.0
coins_value = 0.0

drink_water = 0
drink_milk = 0
drink_coffee = 0
drink_cost = 0.0

def get_drink_details(drink):
    global drink_water
    global drink_milk
    global drink_coffee
    global drink_cost
    drink_water = MENU[drink]['ingredients'].get('water', 0)
    drink_milk = MENU[drink]['ingredients'].get('milk', 0)
    drink_coffee = MENU[drink]['ingredients'].get('coffee', 0)
    drink_cost = MENU[drink]['cost']
    return

def get_resources():
    global machine_balance
    machine_water = resources.get('water', 0)
    machine_milk = resources.get('milk', 0)
    machine_coffee = resources.get('coffee', 0)
    return machine_water, machine_milk, machine_coffee, machine_balance

def enough_resources():
    global drink_water
    global drink_milk
    global drink_coffee
    machine_water, machine_milk, machine_coffee, dummy = get_resources()
    enough_water = machine_water >= drink_water
    enough_milk = machine_milk >= drink_milk
    enough_coffee = machine_coffee >= drink_coffee

    if enough_water and enough_milk and enough_coffee:
        return 0
    elif not enough_water:
        return 1
    elif not enough_milk:
        return 2
    elif not enough_coffee:
        return 3

def process_cost(coins_value):
    global drink_cost
    if drink_cost < coins_value:
        return "balance", coins_value - drink_cost
    elif drink_cost > coins_value:
        return "due", drink_cost - coins_value
    elif drink_cost == coins_value:
        return "settle", 0.0

def accept_coins():
    global coins_value
    global user_money
    quarters = int(input("\nHow many quarters: "))
    dimes = int(input("\nHow many dimes: "))
    nickels = int(input("\nHow many nickels: "))
    pennies = int(input("\nHow many pennies: "))
    coins_value = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    add_coins(coins_value)

def add_coins(coins_value):
    global user_money
    amount_type, amount_value = process_cost(coins_value)
    user_money = amount_value
    if amount_type == 'due':
        return 1
    else:
        return 0

def dispense_drink():
    global coins_value
    resource_flag = enough_resources()
    currency_flag = add_coins(coins_value)
    if resource_flag == 0:
        if currency_flag == 0:
            return True
        else:
            print("\nSorry! You do not seem to have provided enough money for the drink!\nRefunding money...\n")
            return False
    elif resource_flag == 1:
        print("\nSorry! The machine does not have enough water!\nRefunding money...\n")
        return False     
    elif resource_flag == 2:
        print("\nSorry! The machine does not have enough milk!\nRefunding money...\n")
        return False
    elif resource_flag == 3:
        print("\nSorry! The machine does not have enough coffee!\nRefunding money...\n")
        return False

def update_machine():
    global drink_water
    global drink_milk
    global drink_coffee
    global drink_cost
    global machine_balance
    global resources

    resources['water'] -= drink_water
    resources['milk'] -= drink_milk
    resources['coffee'] -= drink_coffee
    
    machine_balance += drink_cost
    
    return

def get_coffee():
    choice = int(input("\nWhat would you like?\n1. Espresso\n2. Latte\n3. Cappuccino\n"))
    if choice == 1:
        drink = "espresso"
    elif choice == 2:
        drink = "latte"
    elif choice == 3:
        drink = "cappuccino"
    else:
        print("\nWrong choice!\nPlease try again\n")
        get_coffee()
    
    get_drink_details(drink)
    accept_coins()

    if dispense_drink():
        print(f"\nHere's your {drink}")
        if user_money > 0:
            print(f"\nHere's your change of ${round(user_money, 2)}")
        print("\nEnjoy your drink!\n")
        update_machine()
        try_again = input("\nWanna do more?\nY or N\n").lower()
        if try_again == 'y':
            start_machine()
        else:
            exit()
    else:
        try_again = input("Try again?\nY or N\n").lower()
        if try_again == 'y':
            get_coffee()
        else:
            exit()
    return

def start_machine():
    user_choice = int(input("\nWelcome!\nPlease select your choice:\n1. Get a drink\n2. Fetch machine report\n3. Exit\n"))
    if user_choice == 2:
        machine_water, machine_milk, machine_coffee, machine_amount = get_resources()
        print(f"\nMachine details:\nWater : {machine_water}ml\nMilk : {machine_milk}ml\nCoffee : {machine_coffee}g\nBalance : ${machine_amount}")
        input("\nPress any key to continue...\n")
        start_machine()
    elif user_choice == 1:
        get_coffee()
    elif user_choice == 3:
        exit()
    else:
        print("\nInvalid Selection!\n")
        start_machine()

start_machine()
