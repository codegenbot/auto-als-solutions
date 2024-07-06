def cycpattern_check(a, b):
    if b in a:
        return True
    for i in range(len(b)):
        b = b[1:] + b[0]
        if b in a:
            return True
    return False