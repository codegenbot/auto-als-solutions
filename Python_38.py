```
def decode_cyclic(s: str):
    result = ""
    group = ""
    for char in s:
        if len(group) < 3:
            group += char
        else:
            if len(result) % 3 == 0:
                result += group[2] + group[1] + group[0]
            else:
                result += group[1] + group[0] + group[2]
            group = char
    if group:
        if len(result) % 3 == 0:
            result += group[2] + group[1] + group[0]
        else:
            result += group[1] + group[0] + group[2]
    return result