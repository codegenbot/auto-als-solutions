def sort_third(lst):
    return sorted(
        [
            x[0] if isinstance(x, list) else [] if y % 3 == 0 else [y]
            for x in lst
            for y in (x if isinstance(x, list) else [x])
        ],
        key=lambda x: len(x),
    )