def sort_even(l: list):
    evens = sorted([x for x in l if x % 2 == 0])
    odds = [x for x in l if x % 2 != 0]
    return [i if j == 0 else i for j, (i, k) in enumerate(zip(odds, evens))]