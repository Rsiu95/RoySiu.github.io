logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def check_operation(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

def float_or_int(num):
    if "." in num:
        return float(num)
    else:
        return int(num)

print(logo)

calculating = True

while calculating:
    num1 = input("What's the first number?: ")
    num1 = float_or_int(num1)
        
    operations = ["+", "-", "*", "/"]
    for symbol in operations:
        print(symbol)
        
    operation = input("Pick an operation: ")
        
    num2 = "\n" + input("What's the next number?: ")
    num2 = float_or_int(num2)
            
    calculated_value = check_operation(num1, num2, operation)
        
    print (f"{str(num1)} {operation} {str(num2)} = {calculated_value}")
        
    continuation = input(f"Type 'y' to continue calculating with {calculated_value}, or type 'n' to start a new calculation: ")
        
    if continuation != "y":
        calculated_value = 0
    else:
        continue_calculating = True
        num1 = calculated_value
        while continue_calculating:
            operation = input("Pick an operation: ")
            num2 = "\n" + input("What's the next number?: ")
            num2 = float_or_int(num2)
            new_calculated_value = check_operation(num1, num2, operation)
            print (f"{str(num1)} {operation} {str(num2)} = {new_calculated_value}")
            continuation = input(f"Type 'y' to continue calculating with {new_calculated_value}, or type 'n' to start a new calculation: ")
            if continuation == "y":
                num1 = new_calculated_value
            else:
                break
            