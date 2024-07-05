def car_race_collision(num_cars):
    total_collisions = 0
    for i in range(num_cars):
        total_collisions += i + 1  
    return total_collisions