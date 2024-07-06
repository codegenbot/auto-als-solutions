Here is the completed code:

def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    coeff = xs[0]
    for i in range(1, len(xs)):
        coeff = (coeff * x - xs[i]) / (i * 1.0)
    return round(coeff, 2)