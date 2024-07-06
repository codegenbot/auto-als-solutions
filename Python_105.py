def by_length(arr):
    result = sorted([i for i in arr if 1 <= i <= 9])
    return [names[int(i) - 1] for i in reversed(result)]