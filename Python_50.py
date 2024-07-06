def decode_shift():
    s = input().strip().lower()
    key = len(s) - s.count(' ')
    return "".join([chr((ord(ch)-97+26-key)%26 + 97) if ch.isalpha() and 'a' <= ch <= 'z'
                    else chr(ord(ch)) if ch.isalpha() and not 'a' <= ch <= 'z'
                    else ch for ch in s])