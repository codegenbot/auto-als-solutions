def decode_shift(s: str):
    result = ""
    for ch in s:
        if ch.islower():
            result += chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a"))
        else:
            result += ch
    return result