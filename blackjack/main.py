import random, art
from function import (current_game_information, pick_cards,
                      game_reset,display_final_result, clear_terminal)

"""
    This game follows this process:
    - Ask the user if they are interested in playing a blackjack game
    - If the user select no, the program exit and if yes, the game goes to the next stage
    - The program picks 2 random cards and assigns to the player and select one for the dealer
    - The program displays the picked value to the player and show the one card assigned to the dealer to the player too
    - The program ask the user if the player wants to tap (to pick another card) or stand (not pick a new card)
    - The program then shift the play to the dealer
    - The dealer is the program itself so it runs automatically
    - The program automatically assigns a new card to the dealer to make the dealer's card two as well
    - The program confirms if the value of the assigned card is not greater than 21, if no, it gives the current player
        the ability to play again in terms of tap or stand, and if yes, the system checks the value and print the 
        appropriate message to the winner        
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
new_game = True


while True:
    user_game_start = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    # user_game_start = "y"

    # Starting a new blackjack game
    if user_game_start == "y":
        # Resetting values from the previous game in case of any error
        game_reset(player_cards, dealer_cards)

        # Checking to know whether to clear the screen when the game is starting afresh from the last play
        if not new_game:
            clear_terminal()
        print(art.logo)

        # Setting the starting value for the player and the dealer
        # Also printing the current game stat to the terminal for the player
        player_cards = pick_cards(cards, 2)
        dealer_cards.append(pick_cards(cards, 1))
        current_game_information(player_cards, dealer_cards)

        while True:
            user_next_step = input("Type 'y' to get another card, type 'n' to pass: ")

            # Condition to execute when the player decides to stand instead of tap
            if user_next_step == "n":
                print(".....Dealer's turn.....")
                computer_choice_list = ["y", "n"]
                dealer_cards.append(pick_cards(cards, 1))

                if sum(dealer_cards) > 21:
                    display_final_result(player_cards, dealer_cards)
                    break
                else:
                    while True:
                        computer_choice = random.choice(computer_choice_list)

                        if computer_choice == "n":
                            display_final_result(player_cards, dealer_cards)
                            break
                        elif computer_choice == "y":
                            dealer_cards.append(pick_cards(cards, 1))

                            if sum(dealer_cards) > 21:
                                display_final_result(player_cards, dealer_cards)
                                break

                break

            # Condition to execute when the player decides to tap instead of stand
            elif user_next_step == "y":
                player_cards.append(pick_cards(cards, 1))

                if sum(player_cards) > 21:
                    display_final_result(player_cards, dealer_cards)
                    break

                current_game_information(player_cards, dealer_cards)

        new_game = False

    elif user_game_start == "n":
        break
