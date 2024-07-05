def sort_even(l: list):
    even = sorted([x for x in l if x % 2 == 0])
    odd = sorted([x for x in l if x % 2 != 0])

    return [i[0] if i else j.pop(0) for i, j in zip(even, [iter(odd)] * len(even))]