def sort_third(lst):
    return [
        (
            sorted(x[2:])
            if isinstance(x, list) and len(x) >= 3
            else [x] if not isinstance(x, list) else [x]
        )
        for x in lst
    ]