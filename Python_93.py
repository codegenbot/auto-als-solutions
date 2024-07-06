def encode(message):
    result = ''
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            offset = ord('a') - ascii_offset if char.islower() else ord('A') - ascii_offset
            result += chr((ord(char) - ascii_offset + offset) % 26 + ascii_offset)
        else:
            result += char
    return result