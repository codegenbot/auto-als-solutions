def find_pair(nums):
    num_dict = {}
    for num in nums[1:]:
        target = nums[0]
        complement = target - num
        if complement in num_dict:
            return str(num) + "\n" + str(complement)
    return "No solution found"