bounciness_index = float(input("Enter the bounciness index: "))
num_bounces = int(input("Enter the number of bounces: "))

total_distance = (1 - 0.5**num_bounces) * bounciness_index
print(total_distance)