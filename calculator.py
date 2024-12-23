import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_accumulate = True
    num1 = float(input("Choose a first number: "))

    while should_accumulate:
        for symbols in operation:
            print(symbols)
        choose_operator = input("Choose an operation: ")
        if choose_operator.isdigit() or choose_operator.isalpha():
            print("You entered a number or string instead of an operator. Please try again.")
            continue

        num2 = float(input("Chose a second number: "))

        operation_function = operation[choose_operator]

        result = operation_function(num1, num2)

        print(f"{num1} {choose_operator} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()