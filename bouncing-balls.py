```Python
def bouncing_balls():
    h0 = float(input())
    hf = float(input())
    bounciness_index = (2 - hf / h0) ** 0.5  
    num_bounces = int(input())
    total_distance = 2 * sum((1 + bounciness_index) ** i for i in range(1, num_bounces+1)) * h0
    print(f"{total_distance:.4f}")