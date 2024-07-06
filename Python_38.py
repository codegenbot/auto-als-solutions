Here is the solution:

def decode_cyclic(s: str) -> str:
    result = ''
    i = 0
    while i < len(s):
        if (i + 3) <= len(s):
            result += s[i] + s[i+1]
            i += 2
        else:
            result += s[i:]
            break
    return result