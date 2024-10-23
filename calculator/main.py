from function import calculation
import art


print(art.logo)

result = 0
first_number = 0
new_calculation = True

while True:
    if new_calculation:
        first_number = float(input("What's the first number?: "))

    operation = input("+\n-\n*\n/\nPick an operation: ").strip()
    second_number = float(input("What's the next number?: "))

    result = calculation(first_number, second_number, operation)

    print(f"{first_number} {operation} {second_number} = {result}")

    user_step_over = input(f"Type 'y' to continue calculating with {result}, or 'no' to start a new calculation:\n").lower()

    if user_step_over == "y":
        first_number = result
        new_calculation = False
    else:
        new_calculation = True


