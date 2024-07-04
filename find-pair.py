def find_pair(nums, target):
    num_set = set()
    for num in nums:
        if target - num in num_set:
            return num, target - num
        num_set.add(num)


if __name__ == "__main__":
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    result = find_pair(nums, target)
    if result:
        print(result[0])
        print(result[1])