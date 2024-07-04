starting_height = float(input())
first_bounce_height = float(input())
num_bounces = int(input())

bounciness_index = first_bounce_height / starting_height
total_distance = starting_height  # Initial drop

current_height = first_bounce_height  # First bounce height

for _ in range(1, num_bounces + 1):
    total_distance += 2 * current_height  # Down and Up
    current_height *= bounciness_index

print(total_distance)