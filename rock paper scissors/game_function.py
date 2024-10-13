def colored_text(text, color_code):
    # Color codes
    # RED = '31'
    # GREEN = '32'
    # YELLOW = '33'
    # BLUE = '34'
    # MAGENTA = '35'
    # CYAN = '36'
    # WHITE = '37'

    return f"\033[{color_code}m{text}\033[0m"



# This function display the diagram in relation to the program input
def print_appropriate_diagram(diagram, value):
    # rock = 0
    # paper = 1
    # scissors = 2

    result = ""

    if value == 0:
        result = diagram.user_rock
    elif value == 1:
        result = diagram.user_paper
    elif value == 2:
        result = diagram.user_scissor

    return result


# This function handles the logic in determining the result of a round
def game_result(user, computer):
    # rock = 0 # paper = 1 # scissors = 2

    # Rock wins against scissors.
    # Scissors win against paper.
    # Paper wins against rock.

    result = ""

    # colored_text("Draw!!", color_code)
    # colored_text("You win!!", "31")
    # colored_text("You lose!!", "32")
    if user == computer:
        result = colored_text("DRAW!!", "33")

    elif user == 0 and computer == 2:
        result = colored_text("You win!!", "32")
    elif user == 2 and computer == 0:
        result = colored_text("You lose!!", "31")

    elif user == 2 and computer == 1:
        result = colored_text("You win!!", "32")
    elif user == 1 and computer == 2:
        result = colored_text("You lose!!", "31")

    elif user == 1 and computer == 0:
        result = colored_text("You win!!", "32")
    elif user == 0 and computer == 1:
        result = colored_text("You lose!!", "31")

    return result

# This function display the diagram in relation to the program input
# and shows them beside each other (UNDER-DEVELOPMENT)
def modified_print_appropriate_diagram(diagram, value, player):
    # rock = 0
    # paper = 1
    # scissors = 2

    result = ""

    if player == "user":
        if value == 0:
            result = diagram.user_rock
        elif value == 1:
            result = diagram.user_paper
        elif value == 2:
            result = diagram.user_scissor

    elif player == "computer":
        if value == 0:
            result = diagram.computer_rock
        elif value == 1:
            result = diagram.computer_paper
        elif value == 2:
            result = diagram.computer_scissor

    return result
