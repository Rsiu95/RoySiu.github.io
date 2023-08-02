from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

def get_coffee():
    
    user_selection = input("What would you like? (" + coffee.get_items() + "): ")
    if user_selection == "off":
        exit
    elif user_selection == "report":
        machine.report()
        money.report()
        get_coffee()
    else:
        drink = coffee.find_drink(user_selection)
        is_sufficient = machine.is_resource_sufficient(drink)
        
        if is_sufficient and money.make_payment(drink.cost):
            machine.make_coffee(drink)
            get_coffee()
        
get_coffee()