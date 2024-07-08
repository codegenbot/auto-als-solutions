def basement(arr):
    total_sum = 0
    found_basement_index = -1
    for i in range(len(arr)):
        total_sum += arr[i]
        if total_sum < 0:
            found_basement_index = i + 1
            break
    return found_basement_index if found_basement_index != -1 else -1