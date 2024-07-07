```
def dice_game(n, m):
    return sum((n - i) / (n + m - 2) for i in range(1, m)) / m