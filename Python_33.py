```
def sort_third(lst):
    return sorted((x if not isinstance(x, tuple) else x for x in lst))