def sort_third(l: list):
    return [
        x if i % 3 != 0 else sorted((y, j) for j, y in enumerate(l) if (j - l.index(y)) % 3 != 0)[0][1]
        for i, x in enumerate(l)
    ]