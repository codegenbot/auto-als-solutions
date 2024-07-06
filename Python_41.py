def car_race_collision(n: int):
    return sum((i - 1) * i for i in range(2, 2 * n))