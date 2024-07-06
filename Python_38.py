```Python
def decode_cyclic(s: str):
    result = ""
    group = ""
    if group:
        if len(group) == 1:  
            result += group
        else:
            if len(result) % 3 == 0:
                result += group[2] + group[1] + group[0]
            else:
                result += group[1] + group[0] + group[2]
    for char in s:
        group += char
        if len(group) == 3:
            if len(result) % 3 == 0:
                result += group[2] + group[1] + group[0]
            else:
                result += group[1] + group[0] + group[2]
            group = ""
    return result