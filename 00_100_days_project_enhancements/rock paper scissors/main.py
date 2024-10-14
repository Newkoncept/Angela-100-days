from random import randint
import diagram, game_function

'''
TODO:::

Two player, Playing against the computer
Hiding user input to prevent cheating
Adding congratulatory gif or ascii art
Making the diagram show beside each other

'''
game_plan = int(input("""Welcome to the game!!!
    Do you want:
    1. Multiplayer (2 player)
    2. Single player\n"""))

if game_plan > 2 or game_plan < 1:
    print(f"\nError: Invalid entry!!!!")
else:
    if game_plan == 1:
        user1_choice = int(input("""User 1 Player: What do you choose?
        Type
        0 for Rock
        1 for Paper
        2 for Scissors\n"""))

        user2_choice = int(input("""User 2 Player: What do you choose?
        Type
        0 for Rock
        1 for Paper
        2 for Scissors\n"""))

        if user1_choice > 2 or user1_choice < 0 :
            print(f"\nError: User 1 entered an invalid entry!!!!")
        elif user2_choice > 2 or user2_choice < 0 :
            print(f"\nError: User 2 entered an invalid entry!!!!")

        else:
            print("User1 chose: \t\t\t\t\t User2 chose:")
            print(game_function.modified_print_appropriate_diagram(diagram, user1_choice, user2_choice))

            print(f"\nResult: {game_function.game_result(user1_choice, user2_choice, game_plan)}")

    else:
        computer_choice = randint(0, 2)
        user_choice = int(input("""What do you choose?
            Type
            0 for Rock
            1 for Paper
            2 for Scissors\n"""))


        if user_choice > 2 or user_choice < 0:
            print(f"\nError: Invalid entry!!!!")
        else:
            print("User1 chose: \t\t\t\t\t Computer chose:")
            print(game_function.modified_print_appropriate_diagram(diagram, user_choice, computer_choice))

            print(f"\nResult: {game_function.game_result(user_choice, computer_choice, game_plan)}")
