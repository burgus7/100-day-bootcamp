from calculator_art import logo

def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

def exponent(first, second):
    return first ** second

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent
}

def new_calculation():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    op_symbol = input("Pick an operation: ")
    while True:
        if op_symbol not in operations:
            op_symbol = input("Pick a valid operation: ")
        else:
            break
    num2 = float(input("What is the next number?: "))

    calc_function = operations[op_symbol]
    answer = calc_function(num1, num2)

    print(f"{num1} {op_symbol} {num2} = {answer}")
    return answer

def cont_calculation(last_answer):
    op_symbol = input("Pick another operation: ")
    while True:
        if op_symbol not in operations:
            op_symbol = input("Pick a valid operation: ")
        else:
            break
    num3 = float(input("What's the next number?: "))
    calc_function = operations[op_symbol]
    answer = calc_function(last_answer, num3)
    return answer

answer = new_calculation()
while True:
    cont = input(f"Type 'y' to continue calculating with {answer}, \n  or type 'n' to start a new calculation,\n  or anything else to exit: ")
    if cont == 'y':
        answer = cont_calculation(answer)
    elif cont == 'n':
        answer = new_calculation()
    else:
        print("Bye!")
        break
