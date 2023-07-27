def tip_calculator():
    print("Welcome to the tip calculator!")
    
    total_bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    bill_split = int(input("How many people to split the bill?"))
    
    individual_amount = round(((total_bill + (total_bill * (tip/100))) / bill_split),2)
    
    return "Each person should pay: $" + str(individual_amount)

print(tip_calculator())
