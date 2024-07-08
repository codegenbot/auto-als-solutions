def basement(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if total < 0:
            break
    else:
        return -1
    return i+1