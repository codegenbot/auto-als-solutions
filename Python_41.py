```
def car_race_collision(num_cars):
    total_collisions = 0
    for i in range(1, num_cars+1):
        collisions_with_others = i-1 
        total_collisions += collisions_with_others 
    return total_collisions

print(car_race_collision(int(input("Enter the number of cars: "))))