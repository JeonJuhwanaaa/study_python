# Calculator

from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_countinue = True

    while should_countinue:
        operation_symbol = input("Pick an operatione: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # operation_symbol = input("Pick another operation: ")
        # num3 = int(input("What's the next number?: "))
        # calculation_function = operations[operation_symbol]
        # second_answer = calculation_function(calculation_function(num1, num2), num3)

        # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to ster a new calculation: ") == "y":
            num1 = answer
        else:
            should_countinue = False
            calculator() # 맨 처음으로 초기화로 새 계산기로 다시 시작

calculator()