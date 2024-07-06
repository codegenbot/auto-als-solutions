```
def decode_shift(s: str):
    return "".join([chr(((ord(ch) - ord('a') if ch.isalpha() else ord(ch)) - 5 - ord("a") if 'a' <= ch <= 'z' else 0) % 26) + ord("a")) if ch.isalpha() and 'a' <= ch <= 'z' else ch for ch in s])