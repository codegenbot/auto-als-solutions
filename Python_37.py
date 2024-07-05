def sort_even(l: list):
    return [
        x if i % 2 != 0 else (next((y for y in l if i % 2 == 0 and y < x), None) if any(y for y in l if i % 2 == 0 and y < x) else None
        for i, x in enumerate(l)
    ]