def car_race_collision(n: int):
    return sum(i * (n - 1) if i < n else (2 * n - i) for i in range(2 * n))