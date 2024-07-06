def decode_shift(s: str):
    key = sum(1 if not ch.isalpha() else 0 for ch in s)
    return "".join([chr((('abcdefghijklmnopqrstuvwxyz'.index(ch.lower())) - 0 + 26 - key) % 26 + 97).lower() if ch.isalpha() and ch.islower() else chr((('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(ch.upper())) - 0 + 26 - key) % 26 + 64) if ch.isalpha() and ch.isupper() else ch for ch in s])