def plain_text_shifter(shift_number, plain):
    cipher = []
    plain_text_length = len(plain)
    shift_text = plain_text_length - shift_number

    cipher.extend(plain[-shift_number:])
    cipher.extend(plain[0:shift_text])

    return cipher


def cipher_text_shifter(shift_number, cipher):
    decipher = []

    decipher.extend(cipher[shift_number:])
    decipher.extend(cipher[:shift_number])

    return decipher


def word_encoder(message, plain, cipher):
    message = message.lower()
    result = ""
    for i in message:
        if i in plain:
            result += cipher[plain.index(i)]
        else:
            result += i

    return result


def word_decoder(message, cipher, decipher):
    message = message.lower()
    result = ""
    for i in message:
        if i in cipher:
            result += decipher[cipher.index(i)]
        else:
            result += i

    return result


def system_reset(cipher, decipher):
    cipher.clear()
    decipher.clear()
