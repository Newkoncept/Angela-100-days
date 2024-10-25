from data import data_set
import random, art

def content_picker():
    game_category = random.choice(list(data_set.keys()))
    return random.choice(data_set[game_category])


def generate_question():
    question = content_picker()
    name = question["name"]
    description = question["description"].replace(".", "")
    country = question["country"]

    final_content = f"{name}, {description}, from {country}"

    return [final_content, question["followers_count"]]


def generate_all_questions():
    first_question = generate_question()
    second_question = generate_question()

    while first_question[0] == second_question[0]:
        second_question = generate_question()

    return [first_question, second_question]



def display_question(first_run, first_question, second_question, score):
    print(art.logo)

    if not first_run:
        print(f"You are right! Current Score: {score}")

    print(f"Compare A: {first_question[0]}")
    print(art.vs)
    print(f"Against B: {second_question[0]}")


def user_pick_answer(first_question, second_question):
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_choice == "A":
        return first_question[1] > second_question[1]
    elif user_choice == "B":
        return second_question[1] > first_question[1]