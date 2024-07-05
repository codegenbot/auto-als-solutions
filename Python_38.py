def decode_cyclic(s: str):
    result = ""
    groups = [s[i:i+3] if i+2 <= len(s) else s[i:] for i in range(0, len(s), 1)]
    for group in groups:
        if len(group) == 2:
            result += group[1]
            result += group[0]
        elif len(group):
            result += group
    return result