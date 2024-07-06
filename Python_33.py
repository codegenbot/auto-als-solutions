def sort_third(lst):
    if isinstance(lst[0], int):
        lst = [(i,) + x for i, x in enumerate(lst)]
    return sorted(lst, key=lambda x: x[2])