def find_pair(nums):
    seen = set()
    for num in nums[1:]:
        target = nums[0] - num
        if target in seen:
            return str(num) + "\n" + str(target)
        seen.add(num)


print(find_pair([int(x) for x in input().split(",")] + [int(input())]))