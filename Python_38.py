def decode_cyclic(s: str):
    result = ""
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
        if len(s) % 3 == 0:
            result += group[2] + group[1] + group[0]
        elif len(result) % 3 != 0:
            while len(group) < 3:
                group += s[0]
                s = s[1:]
            result += group[2] + group[1] + group[0]
    return result