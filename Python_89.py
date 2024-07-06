```
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            value = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - value + 3) % 26 + value)
        else:
            result += char
    return result