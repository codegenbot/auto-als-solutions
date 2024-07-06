def sort_third(lst):
    return sorted(
        [(x // 10000, x % 10000, x % 10000) if isinstance(x, int) else x for x in lst],
        key=lambda x: x[2],
    )