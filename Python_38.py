def decode_cyclic(s: str):
    result = []
    temp = ""
    for char in s:
        temp += char
        if len(temp) == 3:
            if temp[0] != temp[2]:
                while True:
                    if not result or (result[-1][1:] + result[-1][0]) == temp:
                        result.append(temp)
                        temp = ""
                        break
                    elif result[-1][1:] + result[-1][0] < temp:
                        result.append(temp)
                        temp = ""
                        break
                    else:
                        temp = temp[2:] + temp[:2]
            else:
                result.append(temp)
                temp = ""
    if temp:
        if len(temp) == 1 or temp[0] == temp[2]:
            result.append(temp)
        else:
            while True:
                if not result or (result[-1][1:] + result[-1][0]) == temp:
                    result.append(temp)
                    temp = ""
                    break
                elif result[-1][1:] + result[-1][0] < temp:
                    result.append(temp)
                    temp = ""
                    break
                else:
                    temp = temp[2:] + temp[:2]
    return "".join([c[1] if len(c) > 1 else c for c in result])