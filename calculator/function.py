def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2


def calculation(first_number, second_number, operation):
    if operation == "+":
        return add(first_number, second_number)
    elif operation == "-":
        return subtract(first_number, second_number)
    elif operation == "/":
        return divide(first_number, second_number)
    elif operation == "*":
        return multiply(first_number, second_number)

