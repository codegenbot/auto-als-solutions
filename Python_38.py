```
def decode_cyclic(s: str):
    min_len = len(s)
    result = ""

    for i in range(min_len):
        temp_s = s[i:] + s[:i]

        j = 1
        while j < len(temp_s) and temp_s[j-1] != temp_s[0]:
            j += 1
        if j == len(temp_s) or temp_s[j-1] == temp_s[0]: 
            result = temp_s
            break

    return result