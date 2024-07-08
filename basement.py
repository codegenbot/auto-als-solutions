def basement(arr):
    for i, x in enumerate(arr):
        running_sum = 0
        for j in range(i+1):
            running_sum += arr[j]
            if running_sum < 0:
                return i+1
    return -1