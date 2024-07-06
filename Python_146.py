def specialFilter(nums):
    return sum(1 for num in nums if abs(num) > 10 and int(str(abs(num))[-1]) % 2 != 0)