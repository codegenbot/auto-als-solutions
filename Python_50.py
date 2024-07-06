def decode_shift(s: str):
    s = s.upper()
    key = len(s) - s.count(' ')
    return "".join([chr((ord(ch.lower()) - 65 + 26 - key) % 26 + 65) if ch.isalpha() else (ch if ch != ' ' else ' ') for ch in s])