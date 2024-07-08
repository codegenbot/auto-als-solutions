def bouncing_balls():
    h0 = float(input())
    hf = float(input())
    bounciness_index = hf / h0
    num_bounces = int(input())
    total_distance = (2 * h0) / (1 + bounciness_index) * num_bounces
    print(f"{total_distance:.4f}")