import math

starting_height = float(input())
first_bounce_height = float(input())
num_bounces = int(input())

bounciness_index = first_bounce_height / starting_height
total_distance = starting_height

for i in range(1, num_bounces + 1):
    bounce_height = starting_height * (bounciness_index ** i)
    total_distance += 2 * bounce_height

print(total_distance - bounce_height)