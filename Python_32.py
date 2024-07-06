Here is the completed code:

def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    a = xs[0]
    b = xs[1] if len(xs) > 1 else 0
    c = poly([b, -a], -b / (2 * a)) if a != 0 else 0
    return round(c, 2)