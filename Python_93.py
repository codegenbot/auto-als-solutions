def encode(message):
    result = ''
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            offset = -25 if char.isupper() else 3
            result += chr((ord(char) - ascii_offset + offset) % 26 + ascii_offset)
        else:
            result += char
    return result