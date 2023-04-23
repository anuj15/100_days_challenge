from art import coffee
from data import coffee_menu, coffee_resources

profit = 0


# take order
def take_order():
    print(coffee)
    order = input(f"What order you want to place?\n1. espresso: ${coffee_menu['espresso']['cost']}\n2. latte: "
                  f"${coffee_menu['latte']['cost']}\n3. cappuccino: ${coffee_menu['cappuccino']['cost']}\n")
    if order in ['espresso', 'latte', 'cappuccino']:
        check_resources(order)
        take_order()
    elif order == 'report':
        show_report()
    elif order == '0':
        return
    else:
        print("Invalid input. Order again!\n")
        take_order()


def show_report():
    print(f"Milk Left: {coffee_resources['milk']}")
    print(f"Water left: {coffee_resources['water']}")
    print(f"Coffee left: {coffee_resources['coffee']}")


# check resources
def check_resources(order):
    if order != 'espresso':
        if coffee_resources['milk'] < coffee_menu[order]['ingredients']['milk']:
            print("We are out of milk!\n")
            return
    if coffee_resources['water'] < coffee_menu[order]['ingredients']['water']:
        print("We are out of water!\n")
        return
    elif coffee_resources['coffee'] < coffee_menu[order]['ingredients']['coffee']:
        print("We are out of coffee!\n")
        return
    calculate_profit(order)


# make order
def calculate_profit(order):
    actual_cost = coffee_menu[order]['cost']
    print("Please insert coins.")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))
    payment = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if payment < actual_cost:
        print(f"There is not enough money. Please pay ${round(actual_cost - payment, 2)} more.")
    elif payment > actual_cost:
        print(f"Take your order from the counter. Enjoy your drink! Here's your change: "
              f"${round(payment - actual_cost, 2)}")
        reduce_resources(order)
    else:
        print("Take your order from the counter. Enjoy your drink!")
        reduce_resources(order)


# reduce resources
def reduce_resources(order):
    if order != 'espresso':
        coffee_resources['milk'] -= coffee_menu[order]['ingredients']['milk']
    coffee_resources['water'] -= coffee_menu[order]['ingredients']['water']
    coffee_resources['coffee'] -= coffee_menu[order]['ingredients']['coffee']


if __name__ == '__main__':
    take_order()
