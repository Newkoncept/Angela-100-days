def set_default_game_value():
    return 4, 4, True

def welcome_message(total_lives):
    print("Welcome to Py HangMan Game")
    print(f"""Instruction:
    - You have {total_lives} lives at the start of the game
    - Guess the value in the game correctly to win
    """)

def generate_dashes(picked_word_length, guessed_list):
    for i in range(0, picked_word_length):
        guessed_list.append("_ ")

def message(life_remaining, total_lives, msg = ""):
    print(f"***{msg} You have {life_remaining} out of {total_lives} lives remaining *******")

