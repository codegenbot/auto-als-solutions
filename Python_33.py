```
def sort_third(lst):
    return [x if not isinstance(x, list) else sorted(x[2:]) if len(x) >= 3 else x for x in lst]