def car_race_collision(n: int):
    total_distance = 0
    for i in range(1, n + 1):
        total_distance += (2 * i - 1) * (n * 2 * i)
    return total_distance