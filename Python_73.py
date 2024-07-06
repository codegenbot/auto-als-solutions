def smallest_change(arr):
    arr = arr[::-1]
    changes = sum(1 for a, b in zip(arr, arr[1:]) if a != b)
    return changes