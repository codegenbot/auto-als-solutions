def sort_third(lst):
    return sorted([i for i in lst], key=lambda x: (3 if isinstance(x, int) else x[2]))