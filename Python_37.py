```
def sort_even(l: list):
    return [
        x if i % 2 != 0 else (min(y for y in l if i % 2 == 0 and y < x) if any(i % 2 == 0 and y < x for y in l) else None)
        for i, x in enumerate(l)
    ]