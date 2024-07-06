```
def modp(n: int, p: int):
    if p == 2:
        return n % p
    t = modp(n, p // 2)
    return (t * t) % p