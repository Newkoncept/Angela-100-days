from function import (coffee_machine_report_getter,
                      coffee_machine_report_setter,
                      is_resources_sufficient, request_processing_message_displayer,
                      request_coffee_amount, is_amount_sufficient)

from data import possible_user_choice



current_machine_stat = coffee_machine_report_setter()
while True:
    user_choice = input("""What would you like? Type
    'espresso' or 'e'
    'latte' or 'l'
    'cappuccino' or 'c': \n""").lower()

    if user_choice == "report" or user_choice == "r":
        coffee_machine_report_getter(current_machine_stat)

    elif user_choice == "off" or user_choice == "o":
        request_processing_message_displayer(7, "Powering off")
        print("Machine powered off successfully")
        break

    elif user_choice in possible_user_choice:
        # Logic to confirm for sufficient resources
        resources_sufficient = is_resources_sufficient(current_machine_stat, user_choice)

        # Logic to be processed when the machine contains enough resources to process the new order
        if resources_sufficient["is_correct"]:
            user_choice = resources_sufficient["user_drink"]
            user_drink_cost = resources_sufficient["user_drink_cost"]

            # Logic to process coins to buy the necessary drink
            user_amount_inserted = request_coffee_amount(user_choice, user_drink_cost)

            # Logic to check if transaction is successful
            transaction_successful = is_amount_sufficient(user_amount_inserted, user_drink_cost)

            # Logic to process if the user inserted the right amount or more
            if transaction_successful["amount_enough"]:
                coffee_machine_report_setter(current_machine_stat, user_choice)

                # Printing the remaining amount left as change to the user
                print(transaction_successful["message"])
                request_processing_message_displayer(4, "Processing your order")
                print(f"Here is your {user_choice} ☕. Enjoy!")
            else:
                # Printing error message to notify the user that the inserted amount is less
                print(transaction_successful["message"])

        # Printing error message to notify the user that the machine does not have enough resources
        else:
            print(resources_sufficient["message"])

    else:
        print("Invalid entry... Try again")

    print("")
