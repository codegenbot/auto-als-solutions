```
def sort_third(lst):
    return [x for _, x in sorted((y, x) for x in lst for y in [x[2]])]