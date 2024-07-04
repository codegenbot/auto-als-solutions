cipher_from = input().strip()
cipher_to = input().strip()
message = input().strip()

cipher_map = str.maketrans(cipher_from, cipher_to)
deciphered_message = message.translate(cipher_map)

print(deciphered_message)