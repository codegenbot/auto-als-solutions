```
def bouncing_balls():
    h0 = float(input())
    hf = float(input())
    bounciness_index = hf / h0
    num_bounces = int(input())
    total_distance = 0.0
    for i in range(1, num_bounces + 2):
        height = (h0 * (bounciness_index ** i)) if i % 2 == 1 else (h0 * ((1 - bounciness_index) ** i))
        total_distance += abs(height)
    print(f"{total_distance:.4f}")


bouncing_balls()