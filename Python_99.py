def closest_integer(value):
    num = float(value)
    return (
        round(num)
        if abs(num - int(num)) < 0.5
        else int(round(num)) if num > 0 else int(-round(-num))
    )