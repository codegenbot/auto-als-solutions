def decode_cyclic(s: str):
    result = ""
    group = ""
    for char in s:
        if char == "(":
            group += "("
        elif char == ")":
            if len(group) % 3 != 0:
                result += ")" + group[:-1]
            else:
                result += ")" + group[2] + group[1] + group[0]
            group = ""
        else:
            group += char
    if group:
        if len(group) % 3 == 0:
            result += ")" + group[2] + group[1] + group[0]
        else:
            result += ")" + group[1] + group[0] + group[2]
    return result