def bouncing_balls():
    h0 = float(input())
    hf = float(input())
    bounciness_index = hf / h0
    num_bounces = int(input())
    total_distance = (num_bounces * 2 + 1) * h0 / (1 - bounciness_index)
    print(f"{total_distance:.4f}")


bouncing_balls()