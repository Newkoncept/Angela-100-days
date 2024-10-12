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
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
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

direction = input("Where do you want to go? Left or Right\n").lower()
if direction == "left":
    action = input("Congratulations!!\nWhat do you want to do next? Swim or wait\n").lower()
    if action == "swim":
        print("Sorry... Game Over!!!!\nYou got attacked by trout.")
    elif action == "wait":
        door = input("Congratulations!!\nWhich door do you want to take? Red, Blue, Yellow\n").lower()
        if door == "red":
            print("Sorry... Game Over!!!!\nYou got burned by fire.")
        elif door == "yellow":
            print("Congratulations!!!!!!!!!!!!\nYou Win!!!!!!!!")
        elif door == "blue":
            print("Sorry... Game Over!!!!\nYou got eaten by beasts.")
        else:
            print("Sorry...\nGame Over!!!! Invalid entry")
    else:
        print("Sorry...\nInvalid entry")
elif direction == "right":
    print("Game Over!!!!\nYou fell into a hole")
else:
    print("Invalid entry")