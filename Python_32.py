```
def find_zero(xs):
    n = len(xs)
    if n % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    a = xs[-1]
    b = -sum([coeff for i, coeff in enumerate(xs[:-1]) if i % 2 == 0])
    c = sum([coeff for i, coeff in enumerate(xs[:-1]) if i % 2 != 0])
    d = -a
    x = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    return round(x, 2)