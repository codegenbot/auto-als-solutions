```
def decode_cyclic(s: str):
    result = []
    temp = ""
    for char in s:
        temp += char
        if len(temp) % 3 == 0:
            result.append(temp[1:] + temp[0])
            temp = ""
        elif len(temp) <= 1:
            result.append(temp)
            temp = ""
    if temp:
        result.append(temp)
    return "".join(result)