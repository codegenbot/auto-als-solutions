def decode_cyclic(s: str):
    result = ""
    while len(s) > 0:
        if len(s) >= 2:
            result += s[1] + s[0]
            s = s[2:]
        else:
            result += s[0]
            s = ""
    return result