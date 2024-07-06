def encode(message):
    vowels = "aeiouAEIOU"
    result = ""
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                index = ord(char.lower()) - 97
                new_char = chr((index + 3) % 6 + 97)
                result += new_char.upper() if char.isupper() else new_char
            else:
                if char.islower():
                    result += chr((ord(char) + 3) % 26 + 97)
                else:
                    result += chr((ord(char) - 25) % 26 + 65)
        else:
            result += char
    return result