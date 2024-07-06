```
def smallest_change(arr):
    n = len(arr)
    count = 0
    left, right = 0, n - 1
    while left < right:
        if arr[left] != arr[right]:
            for i in range(n):
                if arr[i] == arr[right]:
                    arr[i], arr[left] = arr[left], arr[i]
                    count += 1
                    break
            right -= 1
        else:
            left += 1
            right -= 1
    return count