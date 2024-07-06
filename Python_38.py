```
def decode_cyclic(s: str):
    result = ""
    group = ""
    for char in s:
        group += char
        if len(group) >= 3:
            if len(result) % 3 == 0:
                result += "".join([group[i] for i in range(2, -1, -1)])
            else:
                result += "".join([group[i] for i in range(1, -1, -1)])
            group = ""
    if group:
        if len(result) % 3 == 0:
            result += "".join([group[i] for i in range(2, -1, -1)])
        else:
            result += "".join([group[i] for i in range(1, -1, -1)])
    return result