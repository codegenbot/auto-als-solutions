def roll_game(n, m):
    return sum(
        1.0 / (m + 1) if i < j else 0 for i in range(1, n + 1) for j in range(1, m + 1)
    ) / (n * m)