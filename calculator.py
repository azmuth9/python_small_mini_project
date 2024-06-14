
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
 '+': add,
 '-': subtract,
 '*': multiply,
 '/': divide
}

def calculator():
    num1 = float(input("What's your first number : "))
    should_continue = True
    while should_continue:
        num2 = float(input("What's your next number : "))
        for symbols in operations:
            print(symbols)
        operations_symbols = input('Pick an operations from the line above : ')
        calculation_function = operations[operations_symbols]
        answer = calculation_function(num1 , num2)
        print(f"{num1} {operations_symbols} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or Type 'n' to exit.") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()