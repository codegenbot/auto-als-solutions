def car_race_collision(): 
    num_cars = int(input("Enter the number of cars: "))
    total_collisions = (num_cars * (num_cars + 1)) // 2 
    return total_collisions

print(car_race_collision())