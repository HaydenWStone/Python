"""
This script implements a simple calculator
"""

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

def calculator():
    def intro():
        print(logo)
        print()
        first_num = float(input("What's the first number?: "))
        print("+")
        print("-")
        print("*")
        print("/")
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        compute(operation,first_num,second_num)

    def add(first_num,second_num):
        solution = float(first_num + second_num)
        return solution
    def subtract(first_num,second_num):
        solution = float(first_num - second_num)
        return solution
    def multiply(first_num,second_num):
        solution = float(first_num * second_num)
        return solution
    def divide(first_num,second_num):
        solution = float(first_num / second_num)
        return solution

    def compute(operation,first_num,second_num):
        if operation == "+":
            output = add(first_num,second_num)
            closing(output,first_num,second_num,operation)
        if operation == "-":
            output = subtract(first_num,second_num)
            closing(output,first_num,second_num,operation)
        if operation == "*":
            output = multiply(first_num,second_num)
            closing(output,first_num,second_num,operation)
        if operation == "/":
            output = divide(first_num,second_num)
            closing(output,first_num,second_num,operation)

    def subsequent(output):
        print("+")
        print("-")
        print("*")
        print("/")
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        first_num = output
        compute(operation,first_num,second_num)

    def closing(output,first_num,second_num,operation):
        print(f"{first_num} {operation} {second_num} = {output}")
        next = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
        if next == "y":
            subsequent(output)
        if next == "n":
            calculator()

    intro()

calculator()





