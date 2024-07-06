```
def closest_integer(value):
    num = float(value)
    if abs(num) % 1 < 0.5:
        return int(round(num))
    else:
        return int(round(num)) + (1 if num > 0 else -1)