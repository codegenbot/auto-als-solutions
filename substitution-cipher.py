def substitute_cipher(ciphertext, cipher_map):
    deciphered_text = ""
    for char in ciphertext:
        if char in cipher_map:
            deciphered_text += cipher_map[char]
        else:
            deciphered_text += char
    return deciphered_text


# Read input from user
cipher_map1 = str(input())
cipher_map2 = str(input())
text_to_decrypt = str(input())

# Apply the cipher to the text and print the result
print(
    substitute_cipher(text_to_decrypt, dict(zip(list(cipher_map1), list(cipher_map2))))
)