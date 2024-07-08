```
def bouncing_balls():
    h0 = float(input())
    hf = float(input())
    bounciness_index = hf / (2 * h0)
    num_bounces = int(input())
    total_distance = 2 * (num_bounces + 1) * h0 / (1 - bounciness_index)
    print(f"{total_distance:.4f}")

bouncing_balls()