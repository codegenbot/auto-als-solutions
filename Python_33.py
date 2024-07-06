def sort_third(lst):
    return [sorted(i) if isinstance(i, list) else [i] for i in lst]