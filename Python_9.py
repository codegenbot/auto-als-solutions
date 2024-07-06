```
def max_rolling_sum(lst):
    max_sum = 0
    current_sum = 0
    for num in lst:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        elif current_sum < 0:
            current_sum = 0
    return max_sum

print(max_rolling_sum([1, 2, 3, 4, 5]))