```
def order_by_points(nums):
    return sorted((n, sum(int(digit) for digit in str(abs(n)))) for n in nums)