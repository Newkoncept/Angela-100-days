import random, functions, hangman_words, diagram

picked_word = list(random.choice(hangman_words.words))
picked_word_length = len(picked_word)
guessed_list = []

# print(picked_word)
total_lives, life_remaining, is_active = functions.set_default_game_value()

functions.welcome_message(total_lives)
functions.generate_dashes(picked_word_length, guessed_list)
functions.message(life_remaining, total_lives)

while life_remaining > 0 and is_active:
    print(f"Word to guess: {"".join(guessed_list)}")
    user_input = input("Guess a value: ").lower()

    if user_input not in picked_word:
        life_remaining -= 1
        functions.message(life_remaining, total_lives, "Error:")
        level = f"level_{life_remaining}"
        level_diagram = getattr(diagram, level)
        print(level_diagram)
        if life_remaining < 1:
            print("Game over, you ran out of lives")
    else:
        if user_input + " " in guessed_list:
            functions.message(total_lives, "Correct:")
            print("")
            continue

        functions.message(life_remaining, total_lives, "Correct:")

        for index, value in enumerate(picked_word):
            if value == user_input:
                guessed_list[index] = value + " "

        if "_ " not in guessed_list:
            is_active = False
            print(f"Word to guess: {"".join(guessed_list)}")
            level = f"level_{life_remaining}"
            level_diagram = getattr(diagram, level)
            print(level_diagram)
            print("You escaped and won!!!")

    print("")


