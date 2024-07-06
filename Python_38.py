```Python
def decode_cyclic(s: str):
    result = ""
    temp = []
    for char in s:
        temp.append(char)
        if len(temp) % 3 == 0:
            result += "".join(temp[1:]) + temp[0]
            temp = []
    if temp:
        result += "".join(temp)
    return result