Here is the solution:

def find_zero(xs: list):
    n = len(xs)
    if n % 2 != 0:
        return "Error: The polynomial should have an even number of coefficients."
    x = -xs[1] / (2 * xs[0])
    return round(x, 2)