def sort_third(lst):
    return sorted((y if isinstance(x, tuple) else (x, x) for x in lst))