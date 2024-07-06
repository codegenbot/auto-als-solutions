def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            value = ord(char) - ascii_offset
            value = (value + 3) % 26  
            if char.isupper():
                result += chr((value) + 65)
            else:
                result += chr(value + 97)
        else:
            result += char
    return result