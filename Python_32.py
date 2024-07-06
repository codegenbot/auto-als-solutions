def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")

    n = len(xs)
    m = max(abs(x) for x in xs)

    for x in range(-m * 10, m * 10):
        y = poly(xs, x)
        if abs(y) < 1e-6:  # check for near zero
            return round(x, 2)