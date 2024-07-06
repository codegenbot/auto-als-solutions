def modp(*args):
    n = args[0]
    p = args[1]
    if n < 0:
        n += p

    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, y, x = egcd(b, a % b)
            return (gcd, x, y - (a // b) * x)

    g, _, _ = egcd(n, p)
    if g != 1:
        return None
    else:
        result = pow(0, p-2, p)
        for i in range(p):
            if pow(i, -(p-2), p) == 1:
                result = i
                break
        return result