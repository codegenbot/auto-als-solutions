```
def decode_cyclic(s: str):
    n = len(s)
    if n % 2 == 1:
        s = '0' + s
    result = ""
    groups = [s[i:i+2] for i in range(0, len(s), 2)]
    for group in groups:
        if len(group) == 1:
            result += group * (n // 2)
        else:
            result += group[1] + group[0]
    return result