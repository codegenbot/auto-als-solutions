def decode_cyclic(s: str):
    result = ""
    n = len(s)
    i = 0
    while i < n:
        if s[i] == '(':
            count = 1
            j = i + 1
            for c in s[j:]:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count == 0:
                    break
            result += s[i+1:j]
            i = j
        else:
            result += s[i]
            i += 1
    return result