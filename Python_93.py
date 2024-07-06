Here is the modified code for the given task description and function signature.

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
                index = ord('a' if char.islower() else 'A') + (ord(char) - ord('a')) 
                new_index = (index + 3) % 26 
                result += chr(new_index + ord('a')) if char.islower() else chr(new_index + ord('A'))
        else:
            result += char
    return result