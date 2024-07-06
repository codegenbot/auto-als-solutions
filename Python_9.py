def max_rolling_sum(lst):
    if not isinstance(lst, list) or any(not isinstance(x, int) for x in lst):
        raise ValueError("Input must be a list of integers")
    if len(lst) == 0:
        return 0
    current_max = max_window = sum(lst[:1])
    for window in zip(*[iter(lst)]*2):
        current_max = max(current_max, sum(window))
    return current_max

print(max_rolling_sum([1, 2, 3, 4, 5]))