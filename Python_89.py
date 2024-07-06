```
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            value = ord(char) - ascii_offset
            result += chr((value + 3) % 26 + ascii_offset)
        else:
            result += char
    return result