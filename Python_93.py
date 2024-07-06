```
def encode(message):
    result = ''
    for char in message:
        if char.isalnum():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char.lower()) - ascii_offset + 3) % 26 + ascii_offset)
        else:
            result += char
    return result