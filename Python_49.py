def modp(*args):
    n = args[0]
    p = args[1]
    if n < 0:
        n += p

    def egcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            gcd, y, x = egcd(b, a % b)
            return gcd, y - (a // b) * x, x

    g, y, x = egcd(n, p)
    if g != 1:
        result = None
    else:
        result = pow(x, -(p-2), p)

    return result