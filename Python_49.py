def modp(*args):
    n = args[0]
    p = args[1]
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
        result = None 
    else:
        result = pow(x, -(p-2), p)
    return result