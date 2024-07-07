def find_pair(n):
    target = int(input())
    nums = [int(x) for x in input().split()]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return "{}\n{}".format(nums[i], nums[j])