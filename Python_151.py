def double_the_difference(lst):
    if len(lst) == 0:
        return 0
    else:
        return sum(i ** 2 for i in filter(lambda x: isinstance(x, int) and x >= 0, lst)) * 2