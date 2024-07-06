```
def encode(message):
    result = ''
    for char in message:
        if char.isalpha():
            offset = 2
            if char.isupper():
                result += chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
        else:
            result += char
    return result