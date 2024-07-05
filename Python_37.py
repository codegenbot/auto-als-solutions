def sort_even(l: list):
    return [
        x if i % 2 != 0 else min([y for y in l if i % 2 == 0 and y < x]) or None
        for i, x in enumerate(
            sorted((x for i, x in enumerate(l) if i % 2 == 0), reverse=True)
        )
    ]