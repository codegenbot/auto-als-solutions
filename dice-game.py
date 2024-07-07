def dice_game(n, m):
    return sum(1 / n ** k for k in range(m)) / (n * m)