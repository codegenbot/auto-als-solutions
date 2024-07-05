```
def find_max_value(nums: List[int]) -> int:
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val