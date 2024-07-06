def sort_descending(lst):
    return [i if not isinstance(i, list) else sorted(i, reverse=True) for i in lst]