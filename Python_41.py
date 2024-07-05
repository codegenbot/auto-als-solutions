```
def car_race_collision(num_cars: int) -> int:
    if num_cars < 2:
        return 0
    first_car = 1
    collisions = 0
    for i in range(1, num_cars):
        if (i - first_car) % (first_car + 1) == 0 or i == num_cars - 1:
            collisions += 1
            first_car = i
    return collisions