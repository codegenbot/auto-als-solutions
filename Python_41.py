def car_race_collision():
    "How many unique pairs of collided cars are possible in a race with 'n' number of cars?"
    n = int(input("Enter the number of cars: "))
    return n * (n - 1) // 2