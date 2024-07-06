Here is the completed code:

def decode_cyclic(s: str):
    result = ""
    temp_group = ""
    for char in s:
        if len(temp_group) < 3:
            temp_group += char
            result += temp_group[-1]
        else:
            temp_group = temp_group[1:] + char
            result += temp_group[-1]
    return result