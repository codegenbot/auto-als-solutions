def double_the_difference(target, lst):
    odd_sum = sum(i for i in lst if isinstance(i, int) and i % 2 != 0)
    return abs(sum(i**2 for i in lst if isinstance(i, int) and i > 0) - (2 * odd_sum))

print(double_the_difference(5, [1, 2, 3, 4, 5]))