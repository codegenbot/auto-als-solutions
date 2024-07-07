```
def bouncing_balls():
    start_height = float(input())
    first_bounce_height = float(input())
    bounciness_index = first_bounce_height / start_height
    
    total_distance = 0
    bounce_count = int(input())
    
    for _ in range(bounce_count):
        total_distance += start_height * (1 + bounciness_index)
        start_height *= bounciness_index
        
    return str(round(total_distance, 5))

print(bouncing_balls())