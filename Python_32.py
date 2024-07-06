def find_zero(xs):
    if len(xs) == 2:
        return (-xs[1]) / xs[0]
    elif len(xs) > 2:
        return (-xs[-1]) / xs[-2]