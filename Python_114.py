```
def minSubArraySum(nums):
    if not nums:
        return 0
    min_sum = float('inf')
    left, right = 0, 0
    current_sum = 0
    while right < len(nums):
        current_sum += nums[right]
        if current_sum > 0:
            min_sum = min(min_sum, current_sum)
            while current_sum >= 0 and left <= right:
                current_sum -= nums[left]
                left += 1
        right += 1
    return min_sum