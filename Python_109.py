def move_one_ball(arr):
    if len(arr) == 0:
        return True
    
    n = len(arr)
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    
    return True