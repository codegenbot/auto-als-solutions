def sort_even(l: list):
    return [
        i if i % 2 != 0 else j
        for i, j in zip(sorted([x for x in l if l.index(x) % 2 == 0]), l)
    ]