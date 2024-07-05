```
def car_race_collision(n):
    total_collisions = 0
    for i in range(n):
        for j in range(i+1, n):
            total_collisions += 1
    return total_collisions