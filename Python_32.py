def find_zero(xs: list):
    if len(xs) < 2:
        raise ValueError("xs must have at least two coefficients")
    n = len(xs)
    if n % 2 != 0:
        raise ValueError("xs must have even number of coefficients")

    total_sum = sum((i**2) * coeff for i, coeff in enumerate(xs))
    odd_coeff_sum = sum(coeff for i, coeff in enumerate(xs) if i % 2 == 1)

    x = (-3 * odd_coeff_sum / (4 * total_sum)) ** (0.5)
    return round(x, 2)