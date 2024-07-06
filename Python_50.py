def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 97 if ch.islower() else 97 + ((ord(ch) - 64) % 26))) for ch in s])