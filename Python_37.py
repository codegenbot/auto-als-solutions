```
def sort_even(l: list):
    evens = sorted([x for x in l if x % 2 == 0])
    return [j if i % 2 != 0 else evens[i // 2] for i, j in enumerate(l)]