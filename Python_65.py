def circular_shift(x, shift):
    x = str(x)[::-1]
    return str(int(x[-shift % len(x) :]) + int(x[: -shift % len(x)]))[::-1]