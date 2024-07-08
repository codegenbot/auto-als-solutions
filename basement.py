def basement(arr):
    sum_so_far = 0
    found_basement_index = None
    for i in range(len(arr)):
        sum_so_far += arr[i]
        if sum_so_far < 0:
            found_basement_index = i+1
            break
    return -1 if found_basement_index is None else found_basement_index