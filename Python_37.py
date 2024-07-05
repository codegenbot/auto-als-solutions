def sort_even(l: list):
    return [
        x if i % 2 != 0 else min(y for y in l if i % 2 == 0 and y < x)
        for i, x in enumerate(l)
    ]