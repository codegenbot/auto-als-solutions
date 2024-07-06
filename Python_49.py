```
def modp(n: int, p: int):
    if n < 0:
        n += p
    return pow(n % p, p - 1, p)