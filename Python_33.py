def sort_third(lst):
    return [i if isinstance(i, list) else [i // 3] if i % 3 == 0 else [i] for i in lst]