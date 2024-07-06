```
def encode(message):
    result = ''
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            offset = 3
            shifted_char = chr((ord(char) - ascii_offset + offset) % 26 + ascii_offset)
            result += shifted_char if char.islower() else shifted_char.upper()
        else:
            result += char
    return result