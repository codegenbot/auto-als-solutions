def modp(*args):
    n = args[0]
    p = args[1]
    if n < 0:
        n += p
    
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        elif b == 0:
            return a, 1, 0
        else:
            gcd, y, x = egcd(b, a % b)
            return gcd, y - (a // b) * x, x

    g, y, _ = egcd(p - 2, p)
    result = pow(y % p, -1, p)

    return result