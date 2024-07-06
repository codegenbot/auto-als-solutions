def max_rolling_sum(lst):
    if len(lst) == 0:
        return 0
    max_sum = current_sum = sum(lst[:1])
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_rolling_sum([14, -5, 12]))