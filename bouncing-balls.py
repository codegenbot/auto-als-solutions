from decimal import Decimal, getcontext

getcontext().prec = 50

starting_height = Decimal(input("Enter starting height: "))
first_bounce_height = Decimal(input("Enter first bounce height: "))
num_bounces = int(input("Enter number of bounces: "))

bounciness_index = first_bounce_height / starting_height
total_distance = Decimal(0)
current_height = starting_height

for _ in range(num_bounces):
    total_distance += current_height
    current_height *= bounciness_index
    total_distance += current_height

print(float(total_distance))