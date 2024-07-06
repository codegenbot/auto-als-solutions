```
def find_closest_pair(nums):
    min_diff = float('inf')
    closest_pair = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = nums[j] - nums[i]
            if abs(diff) < abs(min_diff):
                min_diff = diff
                closest_pair = [nums[i], nums[j]]
    return closest_pair