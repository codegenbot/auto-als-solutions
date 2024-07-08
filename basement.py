def basement(arr):
    total_sum = 0
    for i in range(len(arr)):
        if total_sum <= 0:
            start_index = i
            total_sum += arr[i]
        else:
            total_sum += arr[i]
    return start_index + 1 if total_sum < 0 else -1