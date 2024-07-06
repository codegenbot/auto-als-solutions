Here is the modified code:

```
def modp(n: int, p: int):
    if n < 0:
        n += p
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, y, x = egcd(b, a % b)
            return gcd, y - (a // b) * x, x

    g, y, x = egcd(n, p)
    if g != 1:
        return None 
    else:
        return x % p