def game_startup_message():
    print("Welcome to the Py Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")


def game_default_level(difficulty_level):
    if difficulty_level == "easy":
        return 10
    else:
        return 5