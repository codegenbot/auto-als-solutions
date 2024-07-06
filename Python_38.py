def decode_cyclic(s: str):
    result = ""
    i = 0
    while i < len(s):
        if (i + 3) <= len(s):
            result += s[i + 1] + s[i]
            i += 2
        else:
            result += s[i:]
            break
    return result