def decode_cyclic(s: str):
    result = ""
    if len(s) % 3 == 0:
        group += s[len(s)-3:]
    group = ""
    for char in s:
        group += char
        if len(group) == 3:
            if len(result) % 3 == 0:
                result += group[2] + group[1] + group[0]
            else:
                result += group[1] + group[0] + group[2]
            group = ""
    if group:
        if len(result) % 3 == 0:
            result += group[2] + group[1] + group[0]
        elif len(group) == 1:  
            result += group
        else:
            if len(result) % 3 == 1:
                result += group[2] + group[1] + group[0]
            else:
                result += group[1] + group[0] + group[2]
    return result