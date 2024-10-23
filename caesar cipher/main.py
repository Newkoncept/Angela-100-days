from thonny.plugins.statement_boxes import print_tree

from function import plain_text_shifter, cipher_text_shifter, word_encoder, word_decoder, system_reset
plain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher = []
decipher = []

print("Welcome to Py Caesar Cipher")
while True:
    system_reset(cipher, decipher)

    user_choice = input("Type \n'encode' to encrypt \n'decode' to decrypt \n'quit' to exit the program:\n").lower()

    if user_choice == "encode" or user_choice == "decode":
        if user_choice == "encode":
            user_message = input("Type your message:\n")
            user_shift_number = int(input("Type the shift number:\n"))
            cipher.extend(plain_text_shifter(user_shift_number, plain))
            print(f"Here's the encoded result: {word_encoder(user_message, plain, cipher)}")

        elif user_choice == "decode":
            user_message = input("Type your message:\n")
            user_shift_number = int(input("Type the shift number:\n"))

            cipher.extend(plain_text_shifter(user_shift_number, plain))
            decipher.extend(cipher_text_shifter(user_shift_number, cipher))
            print(f"Here's the decoded result: {word_decoder(user_message, cipher, decipher)}")


        user_start_over_option = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

        if user_start_over_option == "no":
            print("Program exiting!!")
            break

    elif user_choice == 'quit':
        print("Program exiting!!")
        break

    else:
        print("Invalid input")
        continue
