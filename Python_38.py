```
def decode_cyclic(s: str):
    result = ""
    while s:
        for i in range(3):
            if i < len(s):
                group += s[0]
                s = s[1:]
            else:
                group += group[len(group) - 2] + group[-1]
                break
        if len(result) % 3 == 0:
            result += group[2] + group[1] + group[0]
        else:
            result += group[1] + group[0] + group[2]
        group = ""
    return result