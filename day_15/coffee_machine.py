from frequent_functions import get_valid_answer, format_list_to_string
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

money = 0 #how much money in machine

emojis = []

# TODO: 1. Main Funct: Ask Flavor, off return
def coffee_machine():
    flavor_options = ['report', 'off', 'espresso', 'latte', 'cappuccino']
    flavor = get_valid_answer(flavor_options, "What would you like? (espresso/latte/cappuccino): ")

    if flavor == 'off':
        return
    elif flavor == 'report':
        report()
    else:
        missing_resources = check_resources(flavor)
        if len(missing_resources) == 0:
            payment(flavor)
        else:
            missing_string = format_list_to_string(missing_resources)
            print(f"Sorry there is not enough {missing_string}.")
    coffee_machine()

# TODO: 2. Report Function
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# TODO: 3. check resource enough
def check_resources(flavor):
    required_resources = MENU[flavor]['ingredients']
    missing = []
    for item in required_resources:
        if required_resources[item] > resources[item]:
            missing.append(resources[item])
    return missing

# TODO: 4. payment function check enough
def payment(flavor):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount_paid = (quarters * 25 + dimes * 10 + nickles * 5 + pennies)/100
    cost = MENU[flavor]['cost']

    if amount_paid < cost:
        print(f"Sorry that's not enough money. Money refunded")
    else:
        change = round(amount_paid - cost, 2)
        if change != 0:
            print(f"Here is ${change} in change.")
        make_drink(flavor)

# TODO: 5. make drink function
def make_drink(flavor):
    flavor_details = MENU[flavor]
    flavor_ingredients = flavor_details['ingredients']
    for item in flavor_ingredients:
        resources[item] -= flavor_ingredients[item]
    print(f"Here is your {flavor} ☕. Enjoy!")
    global money
    money += flavor_details['cost']


coffee_machine()