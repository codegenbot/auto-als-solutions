def sort_even(l: list):
    even = sorted([x for x in l if x % 2 == 0])
    odd = sorted([x for x in l if x % 2 != 0])

    return [i if i % 2 == 0 else next(j) for i, j in zip(even, iter(odd))]