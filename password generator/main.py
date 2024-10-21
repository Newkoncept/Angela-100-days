import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ':', ';', '<', '>', ',', '.', '?', '/', '\\', '|', '~']

total_letters_length = len(letters)
total_numbers_length = len(numbers)
total_symbols_length = len(symbols)


print("Welcome to the PyPassword Generator")
user_letters = int(input("How many letters would you like in your password?\n"))
user_numbers = int(input("How many numbers would you like?\n"))
user_symbols = int(input("How many symbols would you like?\n"))


generated_value = []

# Generating random values for letters
for i in range(0, user_letters):
    random_value = int(random.random() * total_letters_length)
    value = letters[random_value]
    generated_value.append(value)

# Generating random values for numbers
for i in range(0, user_numbers):
    random_value = int(random.random() * total_numbers_length)
    value = numbers[random_value]
    generated_value.append(value)

# Generating random values for symbols
for i in range(0, user_symbols):
    random_value = int(random.random() * total_symbols_length)
    value = symbols[random_value]
    generated_value.append(value)

print(generated_value)

# Randomizing the generated values
randomized_value = []
generated_value_length = len(generated_value)
for i in range(0, generated_value_length):
    selected_value = int(random.random() * len(generated_value))
    randomized_value.append(generated_value[selected_value])
    generated_value.pop(selected_value)

print(randomized_value)

# Final user password
final_password = ""
for i in randomized_value:
    final_password += i

print(f"Your password is: {final_password}")

