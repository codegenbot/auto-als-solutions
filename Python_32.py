def find_zero(xs: list):
    n = len(xs)
    if n % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    x = -sum(coeff for i, coeff in enumerate(xs) if i % 2 == 1) / sum(
        coeff for i, coeff in enumerate(xs) if i % 2 == 0
    )
    return round(x, 2)