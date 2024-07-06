def sort_third(lst):
    return [
        i if isinstance(i, list) else (list(range(j, j + 3)) if i % 3 == 0 else [j])
        for j in lst
    ]