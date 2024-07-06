```
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            value = ((ord(char) - ascii_offset) % 26 + 3) % 26
            result += chr(value + ascii_offset)
        else:
            result += char
    return result