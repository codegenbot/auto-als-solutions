def sort_third(lst):
    return [x[1:] if isinstance(x, list) and len(x) >= 3 else [x] for x in lst]