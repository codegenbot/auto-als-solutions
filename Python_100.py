def make_a_pile(n):
    return [n] + [x for x in range(n+1, n*2) if x % 2 == (n % 2)]