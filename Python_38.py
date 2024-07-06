def encode_cyclic(s: str):
    result = []
    i = 0
    while i < len(s):
        if len(s) - i < 3:
            result.append(s[i:])
            break
        result.append(s[i : i + 3][1:] + s[i : i + 3][0])
        i += 3
    return "".join(result)


def decode_cyclic(s: str):
    result = []
    i = 0
    while i < len(s):
        if len(s) - i < 3:
            result.append(s[i:])
            break
        if len(s[i : i + 3]) == 1:
            result.append(s[i])
        else:
            result.append(s[i + 1] + s[i])
        i += 3
    return "".join(result)