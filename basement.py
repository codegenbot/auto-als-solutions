def basement(arr):
    sum_so_far = 0
    found_basement_index = -1
    for i in range(len(arr)):
        sum_so_far += arr[i]
        if sum_so_far < 0:
            found_basement_index = i+1
            break
    return found_basement_index