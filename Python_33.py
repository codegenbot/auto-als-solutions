```
def sort_third(lst):
    return [i for i in sorted((x[2], x) for x in lst)]