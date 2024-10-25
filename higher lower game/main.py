from function import generate_all_questions, display_question, user_pick_answer, generate_question
from art import logo

player_score = 0
first_run = True
previous_question = []

while True:
    all_questions = generate_all_questions(first_run, previous_question)
    first_question = all_questions[0]
    second_question = all_questions[1]


    display_question(first_run, first_question, second_question, player_score)

    result = user_pick_answer(first_question, second_question)

    if result:
        player_score += 1
        first_run = False
        print("\n" * 100)
        previous_question = second_question

    else:
        print("\n" * 100)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {player_score}")
        break
