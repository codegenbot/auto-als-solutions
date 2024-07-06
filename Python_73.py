def smallest_change(arr):
    n = len(arr)
    arr = [str(x) for x in arr]
    arr = "".join(arr)
    rev_arr = arr[::-1]
    return sum(1 for a, b in zip(arr, rev_arr) if a != b)