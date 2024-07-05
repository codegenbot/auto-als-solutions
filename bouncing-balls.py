from decimal import Decimal, getcontext
import sys

getcontext().prec = 50

input_data = sys.stdin.read().strip().split()
starting_height = Decimal(input_data[0])
first_bounce_height = Decimal(input_data[1])
num_bounces = int(input_data[2])

bounciness_index = first_bounce_height / starting_height
total_distance = Decimal(0)
current_height = starting_height

for _ in range(num_bounces):
    total_distance += current_height
    current_height *= bounciness_index
    total_distance += current_height

print(float(total_distance))