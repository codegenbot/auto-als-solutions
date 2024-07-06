def double_the_difference(lst):
    result = (
        sum(i**2 for i in filter(lambda x: isinstance(x, int) and x >= 0, lst)) * 2
        if lst
        else 0
    )
    return result