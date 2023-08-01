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
    "water": 600,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.1,
    "quarter": 0.25    
}

# checks the usage of each ingredient and returns it in a list
def get_ingredient_usage(coffee_type):
    coffee_ingredients = []
    liquids = [item for item in MENU[coffee_type]["ingredients"]]
    for liquid in liquids:
        coffee_ingredients.append(MENU[coffee_type]["ingredients"][liquid])
    if coffee_type == "espresso":
        coffee_ingredients.insert(1, 0)
    return coffee_ingredients

# access the dict to obtain the cost
def get_coffee_cost(coffee_type):
    return MENU[coffee_type]["cost"]

# access the dict to get the resource
def get_resources(liquid):
    return resources[liquid]

# updates the total resources we have
def update_resources(machine_resources, coffee_usage):
    updated_resources = []
    for resource in range(len(coffee_usage)):
        updated_resources.append(machine_resources[resource] - coffee_usage[resource])
    return updated_resources

# calculates the value of the coins
def calculate_total(coin_type, num_coins):  
    value = coins[coin_type]
    return value * int(num_coins)

# obtains the users coins and returns the total value
def get_user_coins():
    num_quarters = int(input("how many quarters?: "))
    num_dimes = int(input("how many dimes?: "))    
    num_nickles = int(input("how many nickles?: "))
    num_pennies = int(input("how many pennis?: "))
    
    quarters = calculate_total("quarter", num_quarters)
    dimes = calculate_total("dime", num_dimes)
    nickles = calculate_total("nickle", num_nickles)
    pennies = calculate_total("penny", num_pennies)
    return quarters + dimes + nickles + pennies

# create a list of the machine resources, easier to work with
machine_resources = [resources[liquid] for liquid in resources]

# main function
def make_coffee():
    global machine_resources
    
    user_coffee_type = input(("What would you like? (espresso/latte/cappuccino): ")).lower()
    
    # check to ensure that the input value is correct
    if user_coffee_type == "espresso" or user_coffee_type == "latte" or user_coffee_type == "cappuccino":
    
        coffee_cost = get_coffee_cost(user_coffee_type)
        coffee_ingredients = get_ingredient_usage(user_coffee_type)
            
        print("Please insert coins.")
        user_total = get_user_coins()
        
        # checks if the user has entered enough money
        if user_total < coffee_cost:
            print("Sorry that's not enough money. Money refunded.")
            make_coffee()
            
        # user has given enough money
        elif user_total > coffee_cost:
            user_change = user_total - coffee_cost
            
            # store the updated machine resources temporarily
            temp_resources = update_resources(machine_resources, coffee_ingredients)
            
            # check to make sure we haven't gone below our threshold
            for liquid in range(len(machine_resources)):
                if temp_resources[liquid] < 0:
                    no_liquid = list(resources.keys())
                    print(f"Sorry there is not enough {no_liquid[liquid]}.")
                    make_coffee()
            
            # update our machine resources
            machine_resources = temp_resources
            print(f"Here is ${user_change:.2f} in change.\nHere is your {user_coffee_type} ☕. Enjoy!")
            make_coffee()
        else:
            exit
            
    # prompt for another input
    else:
        print(f"We do not sell {user_coffee_type}. Please order something different.")
        make_coffee()
        
make_coffee()