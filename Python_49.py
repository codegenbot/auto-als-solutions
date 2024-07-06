```
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

    g, y, x = egcd(n, p)
    if g != 1:
        result = None
    elif is_prime(p):
        result = None
    else:
        result = pow(x, -(p-2), p)

    return result

def is_prime(num):
    if num < 2: 
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True