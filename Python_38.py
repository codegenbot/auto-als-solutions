def decode_cyclic(s: str):
    result = []
    i = 0
    while i < len(s):
        group = s[i : i + 3]
        if group[0] == group[1]:
            if i + 2 >= len(s):
                return s[: i + 1]
            elif s[i + 1] != group[0]:
                result.append(group[0])
        else:
            if group[0] == group[2]:
                while i < len(s) and s[i] == group[0]:
                    i += 1
            result.append(group[0] + group[1])
        i += 3
    return "".join(result)