```
def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    denominator = x_den * n_den
    numerator = x_num * n_num
    
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    common_divisor = gcd(numerator, denominator)
    
    return bool(denominator // common_divisor)