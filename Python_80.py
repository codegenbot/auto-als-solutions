def is_happy(s):
    if len(s) < 3:
        return False
    s = s.lower()
    for i in range(0, len(s)-2, 3):
        if len(set(s[i:i+3])) != 3 or not set(s[i:i+3]).issubset({'a', 'b', 'c'}):
            return False
    return True