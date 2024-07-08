```
h0 = float(input())
hf = float(input())
bounciness_index = hf / h0
num_bounces = int(input())

def bouncing_balls():
    total_distance = 0
    height = h0
    for _ in range(num_bounces):
        total_distance += 2 * height
        height *= bounciness_index
    print(f"{total_distance:.4f}")