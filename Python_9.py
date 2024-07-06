```
def max_rolling_sum(lst):
    if len(lst) == 0:
        return 0
    current_max = max_window = sum(lst[:1])
    for window in zip(*[iter(lst)]*2):
        current_max = max(current_max, sum(window))
    return current_max

print(max_rolling_sum([1, 2, 3, 4, 5]))