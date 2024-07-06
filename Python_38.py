def decode_cyclic(s: str):
    result = ""
    if len(s) > 0:
        if len(s) >= 2:
            while len(s) >= 2:
                result += s[1] + s[0]
                s = s[2:]
        result += s[0]
    return result