def car_race_collision(n: int):
    if n < 2:
        return "Invalid input. Number of cars must be at least 2."
    else:
        return n * (n - 1)