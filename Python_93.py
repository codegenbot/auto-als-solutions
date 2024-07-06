```
def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                index = ord(char.lower()) - 97
                new_char = chr((index + 3) % 6 + 97)
                result += new_char.upper() if char.isupper() else new_char
            else:
                if char.islower():
                    result += '0' + str(ord(char) - 96)
                else:
                    result += '1' + str(ord(char.lower()) - 96).zfill(2)
        else:
            result += char
    return result