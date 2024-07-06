def decode_shift(s: str):
    key = len(s) - s.count(' ')
    decoded_s = ""
    for ch in s:
        if ch.isalpha():
            shift = ('abcdefghijklmnopqrstuvwxyz'.index(ch.lower()) - 0 + 26 - key) % 26
            if ch.islower():
                decoded_s += chr((shift + 97)).upper()
            else:
                decoded_s += chr((shift + 65))
        else:
            decoded_s += ch
    return decoded_s