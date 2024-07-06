```
def decode_cyclic(s: str):
    if len(s) == 0:
        return s
    
    result = ""
    i = 1
    while len(s) >= i:
        result += s[i - 1]
        s = s[i:]
        i += 2
    
    return result