def double_the_sum_of_squares(lst):
    return sum(i**2 for i in lst if isinstance(i, int) and i > 0) * 2