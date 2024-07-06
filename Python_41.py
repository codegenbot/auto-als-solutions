```
def car_race_collision(n: int):
    total_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            total_distance += 1
    return total_distance