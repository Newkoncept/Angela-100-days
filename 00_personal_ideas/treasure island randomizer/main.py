# This project tries to randomize the result of the treasure island outcome
"""
    -------------------------- GAME SUMMARY: ----------------------------------
    This game tries to make decisions and the program decides the authenticity
    of the answer by comparing the answer with a pre-generated value to determine
    if the user gets to go the next stage of the game, or it's game over for the round.

    The user tries to navigate between different levels. The game has 3 levels.
    The first level ask the user for their direction.
    The second level ask the user for their action based on the direction chosen.
    The third level is the final stage where the user decides on a door to open.


    The game doesn't have a predefined value as the correct answer is defined by
    the program based on a value chosen from a random selection of the program.
"""
from random import random, randint, choice, choices
import jungle_outcome

# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************''')

print("\nWelcome to Treasure Island\nYour mission is to find the treasure.")
possible_direction = ["left", "right"]
possible_action = ["swim", "wait"]
possible_door = ["red", "blue", "yellow"]
final_losing_message = ["You got burned by fire.", "You got eaten by beasts." ]


random_direction = possible_direction[(int(random() * len(possible_direction)))]
direction = input("Where do you want to go? Left or Right\n").lower()
if direction in possible_direction:
    if direction == random_direction:

        random_action = possible_action[(int(random() * len(possible_action)))]
        action = input("Congratulations!!\nWhat do you want to do next? Swim or wait\n").lower()
        if action in possible_action:
            if action == random_action:

                random_door = possible_door[(int(random() * len(possible_door)))]
                door = input("Congratulations!!\nWhich door do you want to take? Red, Blue, Yellow\n").lower()
                if door in possible_door:
                    if door == random_door:
                        print("Congratulations!!!!!!!!!!!!\nYou Win!!!!!!!!")
                    else:
                        print(f"Sorry... Game Over!!!!\n{choice(jungle_outcome.weather_disasters())["description"]}")
                else:
                    print("Sorry...\nGame Over!!!! Invalid entry")

            else:
                print(f"Sorry... Game Over!!!!\n{choice(jungle_outcome.survival_challenges())["description"]}")
        else:
            print("Sorry...\nGame Over!! Invalid entry")
    else:
        print(f"Game Over!!!!\n{choice(jungle_outcome.environmental_dangers())["description"]}")
else:
    print("Invalid entry")