def cycpattern_check(a, b):
    for i in range(len(b)):
        if (b[i:] + b[:i]).encode("utf-8") in a.encode("utf-8"):
            return True
    return False