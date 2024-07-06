def sort_third(lst):
    return [i if isinstance(i, list) else [j for j in range(i, i + 3)] if i % 3 == 0 else [i] for i in lst]