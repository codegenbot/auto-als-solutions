def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char.isalpha():
            if char.upper() in vowels:
                pos = (ord(vowels[vowels.index(char.upper())]) - ord('A') + 2) % 26
                result += chr(ord('A') + pos)
            else:
                if char.isupper():
                    result += 'z' if char == 'Z' else chr(ord('A') + (ord(char) - ord('A')) + 1)
                else:
                    result += 'a' if char == 'a' else chr(ord('a') + (ord(char) - ord('a')) + 1)
        else:
            result += char
    return result