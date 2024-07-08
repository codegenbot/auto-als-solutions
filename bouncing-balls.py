def bouncing_balls():
    h0 = float(input())
    hf = float(input())
    bounciness_index = hf / h0
    num_bounces = int(input())
    total_distance = 2 * (1 + bounciness_index) * num_bounces
    height = h0
    for _ in range(num_bounces):
        if height < 1:
            break
        height *= bounciness_index
    print(f"{total_distance:.4f}")