def circular_shift(x, shift):
    str_x = str(x)[::-1]
    return str(int(str_x[-shift:]) + int(str_x[:-shift])).zfill(len(str_x))