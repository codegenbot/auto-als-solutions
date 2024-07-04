from decimal import Decimal, getcontext

# Set the precision
getcontext().prec = 25

# User inputs with Decimal conversion
starting_height = Decimal(input())
first_bounce_height = Decimal(input())
num_bounces = int(input())

bounciness_index = first_bounce_height / starting_height
total_distance = starting_height

current_height = first_bounce_height

for _ in range(num_bounces - 1):
    total_distance += 2 * current_height
    current_height *= bounciness_index

total_distance += current_height

print(float(total_distance))