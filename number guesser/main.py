import random

from function import game_startup_message, game_default_level


game_startup_message()

user_difficult_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
user_health = game_default_level(user_difficult_level)

value_to_be_guessed = random.randint(1, 100)


while user_health > 0:
    print(f"You have {user_health} attempts remaining to guess the number")

    user_guess = int(input("Make a guess: "))

    if user_guess == value_to_be_guessed:
        print("Value guessed correctly")
        break
    else:
        if user_guess < value_to_be_guessed:
            print("Too low")
        elif user_guess > value_to_be_guessed:
            print("Too high")

        print("Guess again.")
        user_health -= 1
        continue

if user_health < 1:
    print(f"Game over, Your ran out of lives!!\nThe correct value is {value_to_be_guessed}")