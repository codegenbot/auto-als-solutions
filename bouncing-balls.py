starting_height = float(input())
first_bounce_height = float(input())
num_bounces = int(input())

bounciness_index = first_bounce_height / starting_height
total_distance = starting_height  # Initial drop

current_height = first_bounce_height

for _ in range(num_bounces):
    total_distance += 2 * current_height  # Up and down
    current_height *= bounciness_index

total_distance -= current_height  # Remove the last downward bounce as it doesn't happen on the last bounce

print(total_distance)