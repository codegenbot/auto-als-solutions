def sort_third(lst):
    return [i if isinstance(i, list) else [i] for i in lst]