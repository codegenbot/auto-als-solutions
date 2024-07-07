def substitution_cipher(cipher, message):
    deciphered = ""
    for char in message:
        if char.isalpha():
            index = ord(char.upper()) - ord("A")
            deciphered += chr(ord(cipher[index].upper()) + (ord("A") - ord("A")))
        else:
            deciphered += char
    return deciphered


cipher1, cipher2, message = input().split()
print(substitution_cipher(cipher1, message))