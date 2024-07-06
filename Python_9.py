def max_rolling_sum(lst):
    if len(lst) == 0:
        return 0
    current_max = max_window = sum(lst[:1])
    for i in range(1, len(lst)):
        current_max = max(current_max, sum(lst[i-1:i+1]))
    return current_max

print(max_rolling_sum([1, 2]))