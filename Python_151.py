def double_the_difference(lst):
    odd_sum = sum(i for i in lst if isinstance(i, int) and i >= 0 and i % 2 != 0)
    return sum(i**2 for i in lst if isinstance(i, int) and i >= 0 and i % 2 != 0) / (2 * odd_sum)

def check():
    lst = [1, -2, 3, 4, 5]
    return_value = double_the_difference(lst)
    assert round(return_value, 2) == 4.0

check()