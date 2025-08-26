from data import menu, resources
cont=True


def drink(ch):
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies?: "))
    if q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01 < menu['espresso']['cost']:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        if ch =="espresso":
            resources['water']-=menu[ch]['ingredients']['water']
            resources['coffee']-=menu[ch]['ingredients']['coffee']
            resources['money']+=menu[ch]['cost']
        else:
            resources['water'] -= menu[ch]['ingredients']['water']
            resources['coffee'] -= menu[ch]['ingredients']['coffee']
            resources['milk'] -= menu[ch]['ingredients']['milk']
            resources['money'] += menu[ch]['cost']

        print(f'''Your change is ${"{:.2f}".format(q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01 - menu[ch]['cost'])}\nHere is your {ch}''')


while cont:
    c=input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if c=="off":
        cont=False

    if c=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    if c=="espresso":
        if resources['water'] >= menu['espresso']['ingredients']['water'] and resources['coffee'] >= menu['espresso']['ingredients']['coffee']:
            drink(c)
        else:
            if resources['water'] < menu['espresso']['ingredients']['water']:
                print("Sorry, there is not enough water.")
            if resources['coffee'] < menu['espresso']['ingredients']['coffee']:
                print("Sorry, there is not enough coffee.")

    if c=="latte":
        if resources['water'] >= menu['latte']['ingredients']['water'] and resources['coffee'] >= menu['latte']['ingredients']['coffee'] and resources['milk'] >= menu['latte']['ingredients']['milk']:
            drink(c)
        else:
            if resources['water'] < menu['latte']['ingredients']['water']:
                print("Sorry, there is not enough water.")
            if resources['coffee'] < menu['latte']['ingredients']['coffee']:
                print("Sorry, there is not enough coffee.")
            if resources['milk'] < menu['latte']['ingredients']['milk']:
                print("Sorry, there is not enough milk.")

    if c=="cappuccino":
        if resources['water'] >= menu['cappuccino']['ingredients']['water'] and resources['coffee'] >= menu['cappuccino']['ingredients']['coffee'] and resources['milk'] >= menu['cappuccino']['ingredients']['milk']:
            drink(c)
        else:
            if resources['water'] < menu['cappuccino']['ingredients']['water']:
                print("Sorry, there is not enough water.")
            if resources['coffee'] < menu['cappuccino']['ingredients']['coffee']:
                print("Sorry, there is not enough coffee.")
            if resources['milk'] < menu['cappuccino']['ingredients']['milk']:
                print("Sorry, there is not enough milk.")
