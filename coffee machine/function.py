from data import resources, menu, money


def format_user_choice(user_choice):
    """Processes the user’s input to return a standardized, full name for their selection, regardless of whether they enter an abbreviation or the full name. This function ensures consistent output for handling user choices."""

    if user_choice == "espresso" or user_choice == "e":
        return "espresso"
    if user_choice == "latte" or user_choice == "l":
        return "latte"
    if user_choice == "cappuccino" or user_choice == "c":
        return "cappuccino"


def get_needed_drink_details(drink_needed):
    """Retrieves details (ingredients, cost, etc.) for a specified drink based on its name."""

    return menu[drink_needed]


def request_processing_message_displayer(duration, message):
    """Displays a message to inform the user that their request is being processed."""

    value = ".."
    for i in range(1, duration):
        print(f"{value * i} {message} {value * i}")


def coffee_machine_report_getter(current_value):
    """Fetches the current status report of the coffee machine, including resource levels and finances."""

    print("Latest coffee machine stats:")
    print(f"-Water: {current_value["water"]}ml")
    print(f"-Milk: {current_value["milk"]}ml")
    print(f"-Coffee: {current_value["coffee"]}g")
    print(f"-Money: ${current_value["money"]}\n")


def coffee_machine_report_setter(current_value=None, user_choice = "",):
    """Updates the machine's report with new data, such as updated resource levels and earnings."""

    if current_value is None:
        value = resources
        value["money"] = float(0)
    else:
        needed_drink = get_needed_drink_details(user_choice)
        needed_drink_ingredients = needed_drink["ingredients"]
        drink_cost = needed_drink["cost"]

        value = current_value
        value["water"] -= needed_drink_ingredients['water']
        value["milk"] -= needed_drink_ingredients['milk']
        value["coffee"] -= needed_drink_ingredients['coffee']
        value["money"] += drink_cost

    return value


def is_resources_sufficient(machine_stat, user_choice):
    """Checks if the coffee machine has enough resources to make the specified drink."""

    selected_user_drink = format_user_choice(user_choice)
    needed_drink = get_needed_drink_details(selected_user_drink)
    needed_drink_ingredients = needed_drink["ingredients"]
    drink_cost = needed_drink["cost"]

    message = []

    if machine_stat["water"] < needed_drink_ingredients["water"]:
        message.append("water")
    if machine_stat["milk"] < needed_drink_ingredients["milk"]:
        message.append("milk")
    if machine_stat["coffee"] < needed_drink_ingredients["coffee"]:
        message.append("coffee")

    message_length = len(message)

    if message_length < 1:
        return {
            "is_correct": True,
            "message": "",
            "user_drink": selected_user_drink,
            "user_drink_cost": drink_cost,
        }
    else:
        if message_length < 2:
            error_message = f"Sorry there is not enough {message[0]}."
        else:
            value = ""
            for i in message:
                value += i + ", "
            error_message = f"Sorry there is not enough {value[:-2]}."

        return {
            "is_correct": False,
            "message": error_message,
        }


def is_amount_sufficient(amount, user_drink_cost):
    """Verifies that the payment provided is enough to cover the cost of the selected drink."""

    quarters = amount['quarters'] * money['quarters']
    dimes = amount['dimes'] * money['dimes']
    nickles = amount['nickles'] * money['nickles']
    pennies = amount['pennies'] * money['pennies']

    total_inserted_amount = quarters + dimes + nickles + pennies

    if total_inserted_amount < user_drink_cost:
        return {
            "amount_enough": False,
            "message": "Sorry that's not enough money. Money refunded."
        }
    else:
        total_amount_left = round((total_inserted_amount - user_drink_cost), 2)
        if total_amount_left > 0:
            return {
            "amount_enough": True,
            "message": f"Here is ${total_amount_left} in change."
        }
        else:
            return {
            "amount_enough": True,
            "message": ""
        }


def request_coffee_amount(user_choice, user_drink_cost):
    """Prompts the user to input the amount of money they are providing for the coffee order."""

    print(f"You selected {user_choice}. The price is ${user_drink_cost}")
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))


    return {
        "quarters": quarters,
        "dimes": dimes,
        "nickles": nickles,
        "pennies": pennies,
    }
