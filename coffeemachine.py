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

money_balance = 0
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
    
    money_balance = insert_coins - MENU[order]["cost"]
    print(f'Here is {money_balance} $ in change.')
    print(f'Here is your {order}. Enjoy! ')
    return money_balance

money_balance = money_balance()

def resources_left():
    # resources_rest = {}
    # water 
    resources_rest_water = resources["water"]-MENU[order]["ingredients"]['water']
    # milk
    if   
    resources_rest_milk = resources["milk"]-MENU[order]["ingredients"]["milk"]
    # coffee  
    resources_rest_coffee = resources["coffee"]-MENU[order]["ingredients"]['coffee']
    # cost  
    money_balance = insert_coins - MENU[order]["cost"]

    resources_rest = {
    "water": resources_rest_water,
    "milk": resources_rest_milk,
    "coffee": resources_rest_coffee,
}  
    print(f'\nResources left are: ')
    for key, value in resources_rest.items():
      
        print( key, ":", value)

    return resources_rest

resources_left = resources_left()



# money = penny * 0.01 + nickel * 0.05 + dimes * 0.10 + quarter * 0.25 
    

#     resources =- order 
#    if order == "report":
#    return 
        
#
# order je narudba TODO

# def coins_to_money():
# penny = 0.01
# nickel = 0.05 
# dime = 0.10 
# quarter = 0.25 

# money


# resources_left():
# resources_rest = {}
# water resources_rest = resources["water"]-menu[order]["ingredients"]['water']
# milk  resources_rest = resources["milk"]-menu[order]["ingredients"]['milk']
# coffee  resources_rest = resources["coffee"]-menu[order]["ingredients"]['coffee']
# cost  money_afterOrder = money - menu[order]["cost"]


# 2.turn off kao elif turn off

# 3.print report.....


#take_coins ()
#resources_left()