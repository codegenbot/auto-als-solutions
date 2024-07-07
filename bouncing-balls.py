def bouncing_balls():
    h = float(input())
    hb = float(input())
    bounciness_index = hb / h
    num_bounces = int(input())
    total_distance = 0
    for _ in range(num_bounces):
        total_distance += 2 * math.sqrt(hb) * (1 - (hb / h)) ** (_ + 1)
    return str(round(total_distance, 4))


print(bouncing_balls())