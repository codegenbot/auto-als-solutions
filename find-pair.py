def find_pair(n, nums):
    seen = set()
    for num in nums:
        target = n - num
        if target in seen:
            return f"{num} {target}"
        seen.add(num)
    return "No pair found"


n = int(input())
nums = [int(x) for x in input().split()]
print(find_pair(n, nums))