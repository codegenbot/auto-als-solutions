def basement(arr):
    total_sum = 0
    for i in range(len(arr)):
        total_sum += arr[i]
        if total_sum < 0:
            return i + 1
        elif total_sum == 0 and i > 0: 
            total_sum = 0
    return -1