def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 97 if ch.islower() else ord(ch) - 64)) % 26 + 97 if ch.islower() else ord(ch) - 32) for ch in s])