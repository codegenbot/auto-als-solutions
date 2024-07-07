def substitution_cipher(cipher1, cipher2, message):
    deciphered_message = ""
    for char in message:
        for i in range(len(cipher1)):
            if char == cipher1[i]:
                deciphered_message += cipher2[i]
                break
        else:
            deciphered_message += char
    return deciphered_message