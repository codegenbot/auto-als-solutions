```
def decode_cyclic(s: str):
    result = ""
    while len(s) > 0:
        if len(s) >= 2 and s[:2] == "00":
            result += "a"
            s = s[2:]
        elif len(s) >= 1:
            result += s[0]
            s = s[1:]
        else:
            break
    while len(s) > 1 and s[:2] == "00":
        result += "a"
        s = s[2:]
    return result + s