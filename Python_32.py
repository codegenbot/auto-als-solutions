def find_zero(xs: list):
    if len(xs) % 2 != 0:
        return None
    n = len(xs)
    x = -xs[1] / xs[n - 1]
    return round(x, 2)