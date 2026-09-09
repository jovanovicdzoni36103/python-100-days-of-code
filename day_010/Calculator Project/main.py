import art

# PAUSE 1: functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# PAUSE 2: Map
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# PAUSE 3: Dictionary
pause_3_result = operations["*"](4, 8)
print(f"PAUSE 3 test (4 * 8): {pause_3_result}")

def calculator():

    print(art.logo)

    num1 = float(input("first number - "))
    should_continue = True

    while should_continue:
        operation = str(input("What operation do you want to do? "))
        num2 = float(input("second number - "))

        result = operations[operation](num1, num2)
        print(f"result: {result}")

        choice = input(f"Wanna continue, your first number is {result}? y / n").lower()

        if choice == "y":
            num1 = result
        else:
            should_continue = False
            calculator()

calculator()