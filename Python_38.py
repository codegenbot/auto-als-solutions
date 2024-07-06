def decode_cyclic(s: str):
    result = ""
    i = 0
    while i < len(s):
        if s[i] == s[i + 2]:
            result += s[i : i + 3]
            i += 3
        else:
            result += s[i : i + 1] + s[i + 2] + s[i + 1]
            i += 3