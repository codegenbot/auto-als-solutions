def bouncing_ball(start_height, first_bounce_height, num_bounces):
    bounciness_index = first_bounce_height / start_height
    total_distance = 0
    for _ in range(num_bounces):
        start_height = first_bounce_height
        first_bounce_height *= bounciness_index
        total_distance += start_height + first_bounce_height
    return total_distance


start_height = float(input())
first_bounce_height = float(input())
num_bounces = int(input())

print(bouncing_ball(start_height, first_bounce_height, num_bounces))