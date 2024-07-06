```
def check(rolling_max):
    if rolling_max > 10:
        print("The maximum rolling sum is too high")
    else:
        print("The maximum rolling sum is within the limits")

rolling_max = max_rolling_sum([1, 2, 3, 4, 5]); check(rolling_max)