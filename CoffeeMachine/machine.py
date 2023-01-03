from menu import MENU, resources


def check_resources(drink):
    if resources.get('water') >= MENU.get(drink)["ingredients"]["water"]:
        if resources.get('coffee') >= MENU.get(drink)["ingredients"]["coffee"]:
            if 'milk' in MENU.get(drink)["ingredients"]:
                if resources.get('milk') >= MENU.get(drink)["ingredients"]["milk"]:
                    return True
                else:
                    print("not enough milk")
                    return False
            else:
                return True
        else:
            print("not enough coffee")
            return False
    else:
        print("not enough water")
        return False


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    return process_coins(quarters, dimes, nickels, pennies)


def process_coins(quarters, dimes, nickels, pennies):
    inserted = 0
    inserted += (.25 * quarters) + (.10 * dimes) + (.05 * nickels) + (.01 * pennies)
    return inserted


def subtracting(choice):
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    if 'milk' in MENU.get(choice)["ingredients"]:
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    print(f"Here is your {choice}. Enjoy")
    return resources


def coffee_machine():
    profit = 0
    machine_on = True
    while machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "espresso":
            if check_resources("espresso"):
                total = insert_coins()
                if total >= MENU.get(choice)["cost"]:
                    profit += MENU.get(choice)["cost"]
                    total -= MENU.get(choice)["cost"]
                    subtracting(choice)
                    print(f"Here is your change: ${round(total, 2)}")
                else:
                    print("Sorry that's not enough money, money refunded!")
        elif choice == "latte":
            if check_resources("latte"):
                total = insert_coins()
                if total >= MENU.get(choice)["cost"]:
                    profit += MENU.get(choice)["cost"]
                    total -= MENU.get(choice)["cost"]
                    subtracting(choice)
                    print(f"Here is your change: ${round(total, 2)}")
                else:
                    print("Sorry that's not enough money, money refunded!")
        elif choice == "cappuccino":
            if check_resources("cappuccino"):
                total = insert_coins()
                if total >= MENU.get(choice)["cost"]:
                    profit += MENU.get(choice)["cost"]
                    total -= MENU.get(choice)["cost"]
                    subtracting(choice)
                    print(f"Here is your change: ${round(total, 2)}")
                else:
                    print("Sorry that's not enough money, money refunded!")
        elif choice == "report":
            print(f"Water: {resources.get('water')}mL")
            print(f"Milk: {resources.get('milk')}mL")
            print(f"Coffee: {resources.get('coffee')}g")
            print(f"Money: ${profit}")
        elif choice == "off":
            machine_on = False


coffee_machine()
