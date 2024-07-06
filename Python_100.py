def make_a_pile(n):
    return [i + (i % 2) * ((n - i) // 2) for i in range(n)]