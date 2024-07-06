```
def decode_cyclic(s: str):
    result = ""
    i = 0
    while i < len(s):
        if i + 1 >= len(s):
            result += s[i:]
            break
        result += s[i+1] + s[i]
        i += 2
    return result