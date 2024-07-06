```
def smallest_change(arr):
    arr = arr.copy()
    arr.reverse()
    return sum(1 for a, b in zip(arr, reversed(arr)) if a != b)