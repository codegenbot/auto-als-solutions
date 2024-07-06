def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    max_coeff = abs(max(xs))
    min_coeff = abs(min(xs))
    for x in range(-max(abs(x) for x in xs), max(abs(x) for x in xs)+1):
        if round(poly(xs, x), 10) == 0:
            return round(x, 2)
    return None