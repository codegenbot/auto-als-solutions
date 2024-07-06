def find_zero(xs):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    max_coeff = abs(max(xs))
    min_coeff = abs(min(xs))
    for x in range(-max(abs(x) for x in xs), max(abs(x) for x in xs) + 1):
        if round(sum(a * x**i for i, a in enumerate(xs)), 10) == 0:
            return round(x, 2)
    return None