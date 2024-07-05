def oddEven(even, odd):
    return [i if i % 2 == 0 else j for i, j in zip(even, odd)]