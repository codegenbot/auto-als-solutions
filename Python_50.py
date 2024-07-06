```
def decode_shift(s: str):
    s = s.strip()
    decoded_s = ''
    key = 0
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                key = ord(ch) - 97
            else:
                key = ord(ch) - 65
        else:
            decoded_s += ch
        decoded_s += chr((ord(ch.lower())-97+key)%26 + 97) if ch.isalpha() and ch.islower() else chr(ord(ch)) if ch.isalpha() else ch
    return decoded_s