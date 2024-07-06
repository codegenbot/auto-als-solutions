def encode(message):
    result = ''
    for char in message:
        if char.isalnum():
            shift = 3 if not char.isupper() else 3
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if 'a' <= char <= 'z' else chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result