def decode_cyclic(s: str):
    if not s:
        return "Input string cannot be empty."
    if len(s) % 2 != 0:
        return "Input string must have an even length."
    result = ""
    groups = [s[i:i+2] for i in range(0, len(s), 2)]
    for group in groups:
        if len(group) == 1:
            result += group * 3
        else:
            result += group[1] + group[0]
    return result