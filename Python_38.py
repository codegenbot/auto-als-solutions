```
def decode_cyclic(s: str):
    result = ""
    group = ""
    for char in s:
        group += char
        if len(group) % 3 == 0:
            if group[2] == group[1]:
                result += group[0]
            else:
                result += group[0] + group[1] + group[2]
            group = ""
    if group:
        if len(group) % 3 == 0:
            if group[2] == group[1]:
                result += group[0]
            else:
                result += group[0] + group[1] + group[2]
        else:
            result += group[0] + group[1] + group[0]
    return result