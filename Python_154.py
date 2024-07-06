```
def cycpattern_check(a, b):
    if len(b) == 0:
        return True
    for i in range(len(b)):
        if a.replace(b[i:] + b[:i], "") != a:
            return False
    return True