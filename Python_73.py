```
def smallest_change(arr):
    n = len(arr)
    left = right = 0
    count = 0
    
    while left < n // 2:
        if arr[left] != arr[n - left - 1]:
            for i in range(n):
                if arr[i] == arr[n - left - 1]:
                    arr[i], arr[left] = arr[left], arr[i]
                    count += 1
                    break
        else:
            left += 1
    
    return count