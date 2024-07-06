def decode_cyclic(s: str):
    result = ""
    while len(s) > 0:
        if len(s) >= 2:
            if len(s) % 2 == 1: 
                result += s[0] + s[1:]
            else: 
                result = s[-1] + s[:-1]
            s = ""
        else:
            result += s[0]
            s = ""
    return result