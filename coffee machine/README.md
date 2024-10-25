# Coffee Machine Console Application

This project is a console-based coffee machine simulator, allowing users to order drinks, track resources, and process payments through an interactive command-line interface.

## Features

- **Drink Selection**: Users can choose from "Espresso," "Latte," or "Cappuccino" by typing the drink name or its abbreviation (`e`, `l`, `c`).
- **Machine Reporting**: By entering `"report"` or `"r"`, users can view the current resource levels and total earnings.
- **Power Off Option**: Users can power off the machine by entering `"off"` or `"o"`.
- **Resource Management**: The machine checks if there are sufficient ingredients for the selected drink:
  - If ingredients are insufficient, a message is displayed, and no transaction occurs.
  - If ingredients are sufficient, the machine proceeds to payment processing.
- **Payment Processing**: Users are prompted to insert money for their chosen drink:
  - If the amount is sufficient, the machine prepares the drink and returns any excess as change.
  - If the amount is insufficient, the machine informs the user, and the transaction is canceled.
- **Order Processing Messages**: The application provides feedback at each stage of the order process, from resource availability to final delivery.

## How It Works

1. **User Input**: The program starts a loop where the user can enter commands to choose a drink, view the report, or power off the machine.
2. **Drink Selection and Validation**: The machine verifies that the user’s selection is valid, including abbreviations.
3. **Resource Check**: If the chosen drink is available, the program checks if the machine has enough ingredients to fulfill the order.
4. **Payment and Transaction**: The user inserts money, and the machine checks if the payment covers the drink’s cost:
    - **Success**: The machine updates its resource levels and dispenses the drink.
    - **Failure**: The user is notified if funds are insufficient or if there’s a problem with the input.
5. **Feedback and Messaging**: Throughout the process, the machine displays messages to guide the user and indicate any errors or successful transactions.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/coffee-machine
   cd coffee-machine

## Usage

Run `main.py` to start the coffee machine simulation. The program will provide prompts for each available command or action, allowing the user to interact with the machine by selecting drinks, viewing the report, or shutting down the machine. User input options include:

### Example Commands:

- **Order a Drink**: Type `"espresso"` or `"e"` for Espresso, `"latte"` or `"l"` for Latte, `"cappuccino"` or `"c"` for Cappuccino.
- **View Report**: Type `"report"` or `"r"` to display the current status of resources and earnings.
- **Power Off**: Type `"off"` or `"o"` to shut down the coffee machine.

## Modular Functions (Further Development)

The program includes several modular functions to maintain clean code and simplify future development:

1. **`format_user_choice(choice)`**  
   Processes the user’s input to return a standardized, full name for their selection, regardless of whether they enter an abbreviation or the full name. This function ensures consistent output for handling user choices.

2. **`get_needed_drink_details(drink_name)`**  
   Retrieves details (ingredients, cost, etc.) for a specified drink based on its name.

3. **`request_processing_message_displayer(message)`**  
   Displays a message to inform the user that their request is being processed.

4. **`coffee_machine_report_getter()`**  
   Fetches the current status report of the coffee machine, including resource levels and finances.

5. **`coffee_machine_report_setter(new_report)`**  
   Updates the machine's report with new data, such as updated resource levels and earnings.

6. **`is_resources_sufficient(drink_ingredients)`**  
   Checks if the coffee machine has enough resources to make the specified drink.

7. **`is_amount_sufficient(payment, cost)`**  
   Verifies that the payment provided is enough to cover the cost of the selected drink.

8. **`request_coffee_amount()`**  
   Prompts the user to input the amount of money they are providing for the coffee order.

## Example Workflow

Here is an example workflow showing how the coffee machine interacts with the user:

1. The user starts the machine and is prompted to choose a drink or view the report.
2. They enter `"latte"` (or `"l"`), and the machine checks if enough resources are available.
3. If resources are sufficient, the user is prompted to insert payment. For instance, if a latte costs $2.50, the user is prompted to enter at least this amount.
4. If the payment is successful, the machine updates its resource report, deducting ingredients used and adding earnings.
5. The drink is then dispensed, and any change is returned if the user inserted more than required.
6. Throughout each stage, the machine displays appropriate messages to guide the user.
