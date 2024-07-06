def encode(message):
    vowels = "aeiouAEIOU"
    result = ""
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                index = ord(char.lower()) - 97
                new_char = chr((index + 2) % 26 + 97)
                result += new_char.upper() if char.isupper() else new_char
            else:
                new_index = (ord(char.lower()) - 97 + 3) % 26 + 97
                result += chr(new_index).upper() if char.isupper() else chr(new_index)
        else:
            result += char
    return result