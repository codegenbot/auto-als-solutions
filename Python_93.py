Here is the corrected Python code for the given task description and function signature:

```Python
def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                index = ord(char.lower()) - 97
                new_char = chr((index + 2) % 26 + 97)
                result += new_char.upper() if char.isupper() else new_char
            else:
                consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
                index = ord(char.lower()) - 97
                new_char = chr((index + 3) % 26 + 97)
                result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result