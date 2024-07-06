def car_race_collision(n: int):
    return sum((i * (2 * n - i)) for i in range(1, 2 * n))