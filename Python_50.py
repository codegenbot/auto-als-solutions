def decode_shift(s: str):
    key = len(s) - s.count(' ')
    return "".join([chr((('abcdefghijklmnopqrstuvwxyz'.index(ch.lower())) - 0 + 26 - key) % 26 + 97).upper() if ch.isalpha() and ch.islower() else ch for ch in s])