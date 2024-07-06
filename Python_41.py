def car_race_collision(n: int):
    total_distance = n
    for i in range(2, 2 * n):
        total_distance += i - 1
    return total_distance