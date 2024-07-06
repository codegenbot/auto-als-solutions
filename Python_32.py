def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    a = xs[-1]
    for x in (-a / xs[1],):  # Start from here
        if round(poly(xs, x), 10) == 0:
            return round(x, 2)