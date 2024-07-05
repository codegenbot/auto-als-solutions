```Python
def car_race_collision(num_cars):
    total_collisions = 0
    for i in range(1, num_cars+1):
        if i > 1:
            total_collisions += i - 1
    return total_collisions