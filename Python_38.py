```
def decode_cyclic(s: str):
    result = ""
    group = ""
    for char in s:
        if char == '(':
            continue
        group += char
        if len(group) % 3 == 0:
            if len(result) % 3 == 0:
                result += group[2] + group[1] + group[0]
            else:
                result += group[1] + group[0] + group[2]
            group = ""
    if group:
        if len(result) % 3 == 0:
            result += group[2] + group[1] + group[0]
        else:
            result += group[1] + group[0] + group[2]
    return result