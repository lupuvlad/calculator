# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Exponent
def exponent(n1, n2):
    return n1**n2


# Square root
def root(n1, n2):
    return n1**n2


# Modulo
def modulo(n1, n2):
    return n1 % n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": exponent,
  "root": root,
  "%": modulo
}


def calculator():

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        if operation_symbol == "root":
            num2 = 0.5
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"The square root of {num1} = {answer}")
        else:
            num2 = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

