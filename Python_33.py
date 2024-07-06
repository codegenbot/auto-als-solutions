def sort_third(l: list):
    return [
        x if i % 3 != 0 else sorted([y for y in l if (i - y) // 3 == (i - 0) // 3])
        for i, x in enumerate(l)
    ]