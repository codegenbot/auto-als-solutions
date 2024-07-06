```
def encode(message):
    result = ''
    offset = 0
    for char in message:
        if char.isalpha():
            if char.isupper():
                offset = ord('A')
            else:
                offset = ord('a')
            if char.isalpha():
                result += chr((ord(char) - offset + 3) % 26 + offset)
        else:
            result += char
    return result