```
def encode_shift(s: str, n: int):
    return "".join([chr((ord(ch.lower()) - 97 + n) % 26 + 97 if ch.islower() else ord(ch.upper()) - 64) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 97 if ch.islower() else ord(ch) - 64)) % 26 + 97 if ch.islower() else ord(ch) - 32) for ch in s])