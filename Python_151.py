def double_the_difference(lst):
    even_sum = sum(i for i in lst if isinstance(i, int) and i % 2 == 0)
    odd_sum = sum(i for i in lst if isinstance(i, int) and i % 2 != 0)
    
    return abs(sum(i**2 for i in lst if isinstance(i, int)) - (2 * even_sum)) if odd_sum == 0 else abs(even_sum - (2 * odd_sum))
double_the_difference([1, 2, 3, 4])