def oddEven(even, odd):
    return [i if i % 2 == 0 else next(j) for i, j in zip(even, [iter(odd)] * len(even))]