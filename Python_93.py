def encode(message):
    result = ''
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            if char.islower():
                result += chr(((ord(char) - ord('a') + 3) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + 25) % 26) + ord('A'))
        else:
            result += char
    return result