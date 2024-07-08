def basement(arr):
    total = 0
    for i in range(len(arr)):
        total = arr[i]
        while total < 0:
            return i+1
        if total == 0:  
            total = 0
    return -1