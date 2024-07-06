def smallest_change(arr):
    n = len(arr)
    forward = arr.copy()
    backward = arr.copy()[::-1]

    for i in range(n // 2):
        if forward[i] != backward[n - i - 1]:
            forward[i], forward[n - i - 1] = forward[n - i - 1], forward[i]

    return sum(1 for a, b in zip(arr, forward) if a != b)