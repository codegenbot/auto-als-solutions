def basement(arr):
    for i in range(len(arr)):
        sum_so_far = 0
        for j in range(i+1):
            sum_so_far += arr[j]
            if sum_so_far < 0:
                return j+1
    return -1