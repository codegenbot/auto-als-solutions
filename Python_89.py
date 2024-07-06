def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65
            else:
                ascii_offset = 97
            value = ord(char) - ascii_offset
            if value + 3 > 25: 
                result += chr((value % 26) + ascii_offset) 
            else:
                result += chr(value + 3 + ascii_offset)
        else:
            result += char
    return result