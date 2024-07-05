def car_race_collision(n):
    total_collisions = 0
    for i in range(n):
        total_collisions += n - 1 - i
    return total_collisions