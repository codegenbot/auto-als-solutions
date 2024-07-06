```
def max_rolling_sum(nums):
    n = len(nums)
    max_sum = current_sum = sum(nums[:3])
    for i in range(3, n):
        current_sum = current_sum + nums[i] - nums[i-3]
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_rolling_sum([14, -5, 12]))