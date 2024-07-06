def sort_even(l: list):
    return [
        (
            x
            if i % 2 != 0
            else (y for y in sorted([y for y in l if (i - 1) // 2 == (l.index(y)) // 2])).__next__()
        )
        for i, x in enumerate(l)
    ]