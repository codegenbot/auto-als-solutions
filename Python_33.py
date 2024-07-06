def sort_third(lst):
    return sorted((x[2], x) if isinstance(x, (list, tuple)) else ((str(x), [x])) for x in lst)