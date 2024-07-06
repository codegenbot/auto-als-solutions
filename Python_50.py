```
def decode_shift(s: str):
    result = ""
    for ch in s:
        if ch.islower():
            result += chr(((ord(ch) - 97) - 5) % 26 + 97)
        else:
            result += chr(((ord(ch) - 65) - 5) % 26 + 65)
    return result