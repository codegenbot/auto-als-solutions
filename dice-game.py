def dice_game(n, m):
    if n < m:
        return 1
    favorable_outcomes = sum([1 for _ in range(m - 1)])
    probability = favorable_outcomes / (n * m)
    return probability