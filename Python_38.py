def encode_cyclic(s: str):
    return "".join([s[i:i+3][1:] + s[i:i+3][0]] if len(s[i:i+3]) == 3 else s[i:i+3] for i in range((len(s) + 2) // 3)]

def decode_cyclic(s: str):
    result = []
    while len(s) >= 3:
        group = s[:3]
        s = s[3:]
        if group[0] == group[1]:
            result.append(group[0])
        else:
            result.append(group[1] + group[0])
    result.extend(list(s))
    return "".join(result)