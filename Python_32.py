import math


def find_zero(coeffs):
    a, b, c = coeffs
    discriminant = (b**2) - 4 * a * c
    if discriminant < 0:
        raise ValueError("Quadratic equation has no real roots")
    return (-b + math.sqrt(discriminant)) / (2 * a)