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


resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

money = 0


def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"Sorry, there is no enough {item}")
            return False
        return True


def process_coin():
    print("Please inserts the coin")
    total = int(input("How many quarters : ")) * 0.25
    total += int(input("How many dimes : ")) * 0.1
    total += int(input("How many nickles : ")) * 0.05
    total += int(input("How many pennies : ")) * 0.01
    return total


def money_check(fees, cost):
    global money
    if fees >= cost:
        money += cost
        change = round(fees - cost)
        print(f"Here, this is your change ${change}.")
        return True
    else:
        print("Sorry, you've not enough money.")
        return False


def making_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here you are {drink_name}. Enjoy it.")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino) :")
    if choice == "off":
        print("Thanks, you are welcome.")
        is_on = False
    elif choice == "report":
        print(f"water : {resource['water']}ml")
        print(f"milk : {resource['milk']}ml")
        print(f"coffee : {resource['coffee']}g")
        print(f"money : ${money}")
    else:
        order = MENU[choice]
        if resource_sufficient(order["ingredients"]):
            payment = process_coin()
            if money_check(payment, order["cost"]):
                making_coffee(choice, order["ingredients"])
