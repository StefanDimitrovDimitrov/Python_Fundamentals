def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def solve(a, b, operator):
    operators = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operator not in operators:
        raise ValueError("The operator is not correct. Use one of the following: add, multiply, divide, subtract")

    return operators[operator](a, b)


operator = input()
a = int(input())
b = int(input())

print(solve(a, b, operator))

# def solve(a, b, operator):
#     result = None
#
#     if operator == "multiply":
#         result = a * b
#     elif operator == "divide":
#         result = a // b
#     elif operator == "add":
#         result = a + b
#     elif operator == "subtract":
#         result = a - b
#
#     return result
#
# print(solve(a, b, operator))
