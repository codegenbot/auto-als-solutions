def double_the_difference(lst):
    lst.sort()
    return (lst[0] + lst[-1]) * 2


double_the_difference([5, 6])