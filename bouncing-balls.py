```
def bouncing_balls():
    h0 = float(input())
    hf = float(input())
    bounciness_index = hf / h0
    num_bounces = int(input())
    total_distance = 0
    height = h0
    for _ in range(num_bounces):
        if bounciness_index != 1: 
            total_distance -= 1  
            total_distance += 2 * height
        else: 
            total_distance += 2 * height
        height *= bounciness_index
        if height < 1:
            break
    print(f"{total_distance:.4f}")