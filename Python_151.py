def double_the_difference(lst):
    return sum(i**2 for i in lst) * 2 if len(lst) > 0 else 0