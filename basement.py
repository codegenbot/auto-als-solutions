def basement(arr):
    for i in range(len(arr)):
        sum_so_far = sum(arr[:i+1])
        if sum_so_far < 0:
            return i+1
    return -1