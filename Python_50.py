def decode_shift(s: str):
    s = s.replace(' ', '')  
    key = len(s)
    return "".join([chr((ord(ch.lower()) - 97 + 26 - key) % 26 + 97) if ch.isalpha() else ch for ch in s])