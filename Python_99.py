def closest_integer(value):
    num = float(value)
    return round(num) if abs(int(num) - num) > 0.5 else int(num)