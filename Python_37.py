def sort_even(l: list):
    evens = [x for x in l if x % 2 == 0]
    return [j if i % 2 != 0 else k for i, j, k in zip(sorted(evens), l)]