```
def sort_third(lst):
    return sorted([x if not isinstance(x, list) else [sorted(y[2:]) for y in x] or [x] for x in lst], key=lambda x: (isinstance(x, list), sorted(list(x))) or [x])