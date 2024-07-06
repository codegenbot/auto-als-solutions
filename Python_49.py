```
def modp(m, p):
    if m < 0:
        m += p
    gcd = lambda a, b: (b, a % b) if a else (a, 0)
    _, x, _ = gcd(m, p)
    return pow(x, -1*p.bit_length(), p)