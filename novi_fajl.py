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
# 1. take order
def make_order():
    order = input("What would you like: espresso/latte/cappuccino or report? ")
    print (f'You chose {order}.')
    return order

order = make_order()


def insert_coins ():
    penny =  int(input ("How many pennies? "))
    nickel = int(input ("How many nickels? "))
    dime = int(input ("How many dimes? "))
    quarter = int(input ("How many quarters? "))

    entered_money = penny * 0.01 + nickel * 0.05 + dime * 0.10 + quarter * 0.25 
    print (f'You entered {entered_money} $.') 
    return entered_money


insert_coins = insert_coins ()

def money_balance():
    money_balance = 0
    entered_money = insert_coins
    money_balance = entered_money - MENU[order]["cost"]
    print(f'Here is {money_balance} $ in change.')
    print(f'Here is your {order}. Enjoy! ')
 
money_balance()
