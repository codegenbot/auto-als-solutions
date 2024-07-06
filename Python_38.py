```
def decode_cyclic(s: str):
    result = ""
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 2]:
            result += s[i : i + 3]
            i += 3
        else:
            if i < len(s) - 1: 
                result += s[i : i + 1] + s[i + 2] + s[i + 1]
            else:
                result += s[i:] 
            break
    return result