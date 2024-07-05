def find_zero(xs):
    if len(xs) != 2:
        return "Input list must contain exactly two elements"
    return -xs[1] / xs[0]