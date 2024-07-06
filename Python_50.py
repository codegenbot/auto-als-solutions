def encode_shift(s: str, shift: int):
    return "".join([chr((ord(ch) + shift - 97 if ch.islower() else ord(ch) + shift - 64) % 26 + 97 if ch.islower() else ord(ch) + shift - 32) for ch in s])

def decode_shift(s: str, shift: int):
    return "".join([chr(((ord(ch) - shift - 97 if ch.islower() else ord(ch) - shift - 64)) % 26 + 97 if ch.islower() else ord(ch) - shift - 32) for ch in s])