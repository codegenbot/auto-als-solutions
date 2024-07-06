```
def decode_cyclic(s: str):
    result = ""
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(result) % 3 == 0:
            result += group[2] + group[1] + group[0]
        else:
            result += group[1] + group[0] + group[2]
    return result