def simplify(x, n):
    x_numerator, x_denominator = map(int, x.split("/"))
    n_numerator, n_denominator = map(int, n.split("/"))

    common_divisor = min(x_denominator, n_denominator)
    new_x_numerator = x_numerator * (common_divisor // x_denominator)
    new_x_denominator = x_denominator * (common_divisor // n_denominator)

    y_numerator = new_x_numerator * n_numerator
    y_denominator = new_x_denominator * n_denominator

    return y_numerator == y_denominator