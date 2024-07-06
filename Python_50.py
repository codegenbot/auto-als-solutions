def decode_shift(s: str):
    return "".join([chr((ord(ch) - 97 if ch.islower() else ord(ch) - 65) % 26 + 97 if ch.islower() else ord(ch)) for ch in s])