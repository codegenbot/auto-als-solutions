def decode_cyclic(s: str):
    result = ""
    while s:
        group = s[:3]
        if len(group) < 3:
            break
        if len(result) % 3 == 0:
            result += group[2] + group[1] + group[0]
        else:
            result += group[1] + group[0] + group[2]
        s = s[3:]
    return result