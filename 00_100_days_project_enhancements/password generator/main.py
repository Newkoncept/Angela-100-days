import random, password_content

"""
* Randomize 3 three times
* Show the final password
Show the total length of generated values

Advance:
Specify the content
Use the auto generator
Use the auto generator with user specifying the required values
"""

print("Welcome to the PyPassword Generator")
user_letters = int(input("How many letters would you like in your password?\n"))
user_numbers = int(input("How many numbers would you like?\n"))
user_symbols = int(input("How many symbols would you like?\n"))


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



#  total length
