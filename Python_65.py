def circular_shift(x, shift):
    x = str(x)[::-1]
    shift %= len(x)
    return str(int(x[shift:]) + int(x[:shift])).lstrip("0") or "0"