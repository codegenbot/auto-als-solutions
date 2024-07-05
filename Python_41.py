```python
# add your problem description here...

def car_race_collision(num_cars):
    total_collisions = (num_cars * (num_cars + 1)) // 2
    return total_collisions

print(car_race_collision(int(input("Enter the number of cars: "))))