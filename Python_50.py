def decode_shift(s: str):
    key = len(s) - s.count(' ')
    return "".join([chr((('abcdefghijklmnopqrstuvwxyz'.index(ch.lower())) - 0 + 26 - key) % 26 + 97).upper() if ch.isalpha() and ch.islower() else (chr((('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(ch.upper())) - 0 + 26 - key) % 26 + 65) if ch.isalpha() and ch.isupper() else ch for ch in s])