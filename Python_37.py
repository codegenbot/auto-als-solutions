def sort_even(l: list):
    return [x if i % 2 != 0 else y for i, (y, x) in enumerate(sorted((x, y) for x, y in zip(reversed(l[1::2]), l[::2])))]