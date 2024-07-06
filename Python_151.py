def double_the_difference(lst):
    total = sum(i**2 for i in (x for x in lst if isinstance(x, int) and x >= 0))
    return total * 2 if lst else 0