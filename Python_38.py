def decode_cyclic(s: str):
    result = ""
    while len(s) > 1:
        for i in range(len(s)):
            s = s[1:] + s[:1]
        result += s[0]
    return result