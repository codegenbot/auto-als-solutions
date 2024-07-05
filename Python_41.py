def car_race_collision():
    n = int(input("Enter the number of cars: "))
    total_collisions = 0
    for i in range(n):
        total_collisions += n - i - 1
    return total_collisions