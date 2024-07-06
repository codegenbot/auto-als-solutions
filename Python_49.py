```Python
def modp(n: int, p: int):
    if n == 1:
        return 1
    elif pow(n, (p - 1) // 2, p) != p - 1:
        return modp(n, p)
    else:
        return 1