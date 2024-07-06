```
def encode(message):
    result = ''
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            offset = -3 if char.islower() else 25
            encoded_char = chr((ord(char) - ascii_offset + offset) % 26 + ascii_offset)
            result += encoded_char.upper() if char.isupper() else encoded_char
        else:
            result += char
    return result