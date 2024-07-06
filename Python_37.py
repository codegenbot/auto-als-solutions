def sort_even(l):
    evens = [x for i, x in enumerate(l) if i % 2 == 0]
    evens.sort()

    return [x if i % 2 != 0 else evens[(i - 1) // 2] for i, x in enumerate(l)]