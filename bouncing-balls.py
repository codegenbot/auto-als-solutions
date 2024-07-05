from decimal import Decimal, getcontext

getcontext().prec = 50

starting_height = Decimal(input())
first_bounce_height = Decimal(input())
num_bounces = int(input())

bounciness_index = first_bounce_height / starting_height
total_distance = starting_height
current_height = first_bounce_height

for _ in range(num_bounces):
    total_distance += 2 * current_height
    current_height *= bounciness_index

print(float(total_distance))