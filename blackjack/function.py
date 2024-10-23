import random


def pick_cards(cards_to_be_picked_from, number_of_cards):
    if number_of_cards < 2:
        return random.choice(cards_to_be_picked_from)
    else:
        return random.choices(cards_to_be_picked_from, k=number_of_cards)


def current_game_information(player_cards, dealer_cards, game_final=False):
    if game_final:
        print(f"    Your final hand: {player_cards}, current score: {sum(player_cards)}")
        print(f"    Dealer's final hand: {dealer_cards}, current score: {sum(dealer_cards)}")
    else:
        print(f"    Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"    Dealer's first card: {dealer_cards[0]}")


def winner_checker(player_cards, dealer_cards):
    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)

    if player_total > 21:
        return "Bust, you went over. You lose 😤"
    elif dealer_total > 21:
        return "Bust, opponent went over. You win 😁"
    elif player_total == dealer_total:
        return "Draw!!"
    elif player_total > dealer_total:
        return "You have the higher card number. You win 😁"
    elif player_total < dealer_total:
        return "Dealer has higher card number. You lose 😤"


def display_final_result(player_cards, dealer_cards):
    current_game_information(player_cards, dealer_cards, True)
    current_game_stat = winner_checker(player_cards, dealer_cards)
    print(current_game_stat)


def game_reset(list1, list2):
    list1.clear()
    list2.clear()


def clear_terminal():
    print("\n" * 50)