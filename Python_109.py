def move_one_ball(arr):
    if not arr:
        return True
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[max_idx]:
            max_idx = i
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i-1]:
            return False
    return True