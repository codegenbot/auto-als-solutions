def car_race_collision(num_cars=None):
    if num_cars is None:
        num_cars = int(input("Enter the number of cars: "))
    total_collisions = (num_cars * (num_cars + 1)) // 2
    return total_collisions