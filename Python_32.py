```
def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    max_coeff = abs(max(xs))
    min_coeff = abs(min(xs))
    for x in range(-max_coeff, max_coeff+1):
        if round(sum(i * j for i, j in zip(xs, [x**i for i in range(len(xs))])) , 10) == 0:
            return round(x, 2)
    return None