def decode_cyclic(s):
    result = ""
    i = 0
    while i < len(s):
        if (i + 3) <= len(s): 
            for j in range(2, -1, -1):
                result += s[i + j]
        else:
            result += s[i:]
        i += 3
    return result