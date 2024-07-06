```
def decode_cyclic():
    s = input()  
    result = ""
    while len(s) > 0:
        if s:
            result += s[0]
            s = s[1:]
        elif len(s) >= 2:
            result += s[1] + s[0]
            s = s[2:]
        else:
            return result
    return result

print(decode_cyclic())