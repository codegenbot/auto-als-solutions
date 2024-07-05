def sort_even(l: list):
    even = sorted([x for x in l if x % 2 == 0])
    odd = sorted([x for x in l if x % 2 != 0])

    result = []
    i = iter(even)
    j = iter(odd)

    while any(i) or any(j):
        try:
            result.append(next(i))
        except StopIteration:
            pass
        try:
            result.append(next(j))
        except StopIteration:
            pass

    return tuple(result)