def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            value = ord(char) - ascii_offset
            result += chr((value + 3) % 26 + ascii_offset)
        else:
            result += char
    return result