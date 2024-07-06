```
def sort_third(lst):
    return [i for sublist in sorted(map(list, lst)) for i in sublist]