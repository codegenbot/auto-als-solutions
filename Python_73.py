def smallest_change(arr):
    n = len(arr)
    arr_palindromic = arr.copy()
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            arr_palindromic[i] = arr_palindromic[n - i - 1]
    return sum(1 for a, b in zip(arr, arr_palindromic) if a != b)