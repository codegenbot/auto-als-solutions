def sort_even(l: list):
    evens = [x for x in l if x % 2 == 0]
    sorted_evens = sorted(evens)
    return [j if i % 2 != 0 else k for (i, k), j in zip(l, cycle(sorted_evens))]