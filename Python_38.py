def decode_cyclic(s: str):
    result = ""
    groups = [s[i:i+2] for i in range(0, len(s), 2)]
    for group in groups:
        if len(group) == 1:
            result += group * (3 - int(group))
        else:
            result += group[1] + group[0]
    return result