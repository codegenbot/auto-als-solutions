def car_race_collision():
    n = int(input("Enter the number of cars: "))
    track_length = float(input("Enter the length of the track: "))
    if n <= 0:
        print("Please enter a positive integer.")
    elif track_length <= 0:
        print("Please enter a positive real number.")
    else:
        collisions = car_race_collision(n)
        probability = (2 * (n - 1) * track_length) / (n * (n + 1))
        print(f"The number of possible collisions is {collisions}. The probability of collision is {probability:.4f}.")