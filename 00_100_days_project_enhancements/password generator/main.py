import random, password_content


"""
* Randomize 3 three times
* Show the final password
* Show the total length of generated values

Advance:
* Specify the content
* Use the auto generator
* Use the auto generator with user specifying the required values
"""

print("Welcome to the PyPassword Generator")

user_letters = 0
user_numbers = 0
user_symbols = 0
expected_password_length = 0


user_password_choice = int(input("""Type (Press Enter when done selecting your choice)
1. Auto generate password (16 characters)
2. Auto generate password but specify the character length
3. (Advanced): Generate password with specific conditions (letters, numbers, symbols)\n"""))

if user_password_choice == 1:
    expected_password_length = 16
elif user_password_choice == 2:
    asked_password_length = int(input("How many characters do you want? (Minimum of 8 characters)\n"))

    if asked_password_length > 7:
        expected_password_length = asked_password_length
    else:
        print("Wrong input length. You need at least 8 characters")
        asked_password_length = int(input("How many characters do you want? (Minimum of 8 characters)\n"))

        if asked_password_length > 7:
            expected_password_length = asked_password_length
        else:
            print("Invalid input length\nProgram exiting!!!")
            exit(0)
elif user_password_choice == 3:
    user_letters = int(input("How many letters would you like in your password?\n"))
    user_numbers = int(input("How many numbers would you like?\n"))
    user_symbols = int(input("How many symbols would you like?\n"))
    expected_password_length = user_letters + user_numbers + user_symbols
else:
    print("Invalid input\nProgram exiting!!!")
    exit(0)

if user_password_choice == 1 or user_password_choice == 2:
    user_letters = random.randint(3, expected_password_length - 5)
    user_numbers = random.randint(1, expected_password_length - user_letters - 1)
    user_symbols = expected_password_length - user_letters - user_numbers


if expected_password_length < 8:
    print("Invalid input length\nProgram exiting!!!")
    exit(0)
else:
    generated_value = []

    generated_value.extend(random.choices(password_content.letters, k=user_letters))
    generated_value.extend(random.choices(password_content.numbers, k=user_numbers))
    generated_value.extend(random.choices(password_content.symbols, k=user_symbols))

    print(generated_value)
    for i in range(0, 3):
        random.shuffle(generated_value)

    print(generated_value)


    final_password = ''.join(generated_value)
    print(f"Your password is: {final_password}")
    print(f"Your total password length is: {len(final_password)}")

