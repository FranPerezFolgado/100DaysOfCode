from data import resources, MENU, coin_values

def report(money:bool):
    print("\n")
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    if money:
        print("Money: $" + str(resources["money"]) + "")
    print("\n")

def check_resources(coffee_choice:str):
    coffee_recipe = MENU[coffee_choice]
    enough = True
    for ingredient in coffee_recipe["ingredients"]:
        if not resources[ingredient] > coffee_recipe["ingredients"][ingredient]:
            enough = False
    return enough

def insert_coins():
    coins_inserted = {}
    print("Please insert coins: ")
    coins_inserted["quarters"] = float(input("How many quarters?: "))
    coins_inserted["dimes"] = float(input("How many dimes?: "))
    coins_inserted["nickles"] = float(input("How many nickles?: "))
    coins_inserted["pennies"] = float(input("How many pennies?: "))
    return coins_inserted

def process_coins(coins_inserted:dict):
    value_total = 0.0
    for coin in coins_inserted:
        coin_value = coin_values[coin]
        num_coins = coins_inserted[coin]
        value_total += coin_value * num_coins
    return value_total

def process_purchase(value_inserted:float, drink_choice:str):
    drink_price = MENU[drink_choice]["cost"]
    if value_inserted > drink_price:
        change = round(value_inserted - drink_price,2)
        if change > resources["money"]:
            print("Sorry I don't have enough change :(")
            return False
        print(f"Here is ${change}")
        resources["money"] += drink_price
        return True
    elif value_inserted < drink_price:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        resources["money"] += drink_price
        return True

def make_drink(coffee_choice:str):
    print("Report before purchase: ")
    report(False)
    coffee_recipe = MENU[coffee_choice]
    for ingredient in coffee_recipe["ingredients"]:
        resources[ingredient] -= coffee_recipe["ingredients"][ingredient]
    print("Report after purchase: ")
    report(False)
    print(f"Here is your {coffee_choice}. Enjoy!")

test_dict = {
    "dimes" : 1,
    "nickles": 4,
    "quarters" : 4,
    "pennies": 1,
    "dimes": 3
}

#print(process_coins(test_dict))

#process_purchase(4.2, 3.2)
#print(resources)
