from data import data_set
import random, art


def content_picker():
    """This function picks a question from the lists of available questions"""
    game_category = random.choice(list(data_set.keys()))
    return random.choice(data_set[game_category])


def generate_question():
    """This function format the picked question in a usable format for further processing"""
    question = content_picker()
    name = question["name"]
    description = question["description"].replace(".", "")
    country = question["country"]

    final_content = f"{name}, {description}, from {country}"

    return [final_content, question["followers_count"]]


def generate_all_questions(first_run, previous_question):
    """This functions return all the necessary questions for processing,
    and it also performs error checking to prevent the display of the same question
    at the same time"""

    if first_run:
        first_question = generate_question()
        second_question = generate_question()
    else:
        first_question = previous_question
        second_question = generate_question()


    while first_question[0] == second_question[0]:
        second_question = generate_question()

    while first_question[1] == second_question[1]:
        second_question = generate_question()

    return [first_question, second_question]



def display_question(first_run, first_question, second_question, score):
    """This function performs the functionality of displaying the questions,
    necessary art and the current score of the user when the user gets the last question"""
    print(art.logo)

    if not first_run:
        print(f"You are right! Current Score: {score}")

    print(f"Compare A: {first_question[0]}")
    print(art.vs)
    print(f"Against B: {second_question[0]}")


def user_pick_answer(first_question, second_question):
    """This function handles the logic of determining if the value picked
    by the user is the correct or wrong answer"""
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_choice == "A":
        return first_question[1] > second_question[1]
    elif user_choice == "B":
        return second_question[1] > first_question[1]