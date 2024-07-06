```
def check(sum):
    if sum > 10:
        print("The maximum rolling sum is greater than 10.")
    else:
        print("The maximum rolling sum is not greater than 10.")

def max_rolling_sum(lst):
    if len(lst) == 0:
        return 0
    current_max = max_window = sum(lst[:1])
    for window in zip(*[lst[i::2] for i in range(0, len(lst), 2)]):
        current_max = max(current_max, sum(window))
    return current_max

rolling_max = max_rolling_sum([1, 2, 3, 4, 5]); check(rolling_max)