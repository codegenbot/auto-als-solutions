starting_height = float(input())
first_bounce_height = float(input())
num_bounces = int(input())

bounciness_index = first_bounce_height / starting_height
total_distance = 0  # Updated initialization

current_height = starting_height  # Updated current height initialization

for _ in range(num_bounces):
    total_distance += current_height  # Drop
    current_height *= bounciness_index
    total_distance += current_height  # Bounce back up

print(total_distance)