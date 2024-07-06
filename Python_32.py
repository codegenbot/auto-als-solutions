```
def find_zero(xs):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    max_coeff = abs(max(xs))
    min_coeff = abs(min(xs))
    for x in range(-max_coeff, max_coeff+1):
        if round(sum(c*x**(len(xs)-1-i) for i,c in enumerate(reversed(xs)))) == 0:
            return round(x, 2)
    return None