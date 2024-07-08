```
def bouncing_balls():
    h0 = float(input())
    hf = float(input())
    bounciness_index = hf / h0
    num_bounces = int(input())
    total_distance = 2 * sum(h0 * (1 + bounciness_index) ** i for i in range(1, num_bounces + 1))
    print(f"{total_distance:.4f}")