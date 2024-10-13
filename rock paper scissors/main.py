from random import randint
import diagram, game_function

computer_choice = randint(0, 2)
user_choice = int(input("""What do you choose?
    Type
    0 for Rock
    1 for Paper
    2 for Scissors\n"""))


if user_choice > 2 or user_choice < 0:
    print(f"\nError: Invalid entry!!!!")
else:
    print("You chose:")
    print(game_function.print_appropriate_diagram(diagram, user_choice))

    print("\nComputer chose:")
    print(game_function.print_appropriate_diagram(diagram, computer_choice))

    print(f"\n\nResult: {game_function.game_result(user_choice, computer_choice)}")



