```
def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

def modp(n: int, p: int):
    if gcd(n, p) != 1:
        return None
    res = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            p = p // 2
        else:
            res = (res * (2 * p - 1)) % p
            n = n * 2 - 1
            p += 1
    return res