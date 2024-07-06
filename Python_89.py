def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            value = (ord(char) - ascii_offset + 3) % 26
            result += chr(value + ascii_offset)
        else:
            result += char
    return result