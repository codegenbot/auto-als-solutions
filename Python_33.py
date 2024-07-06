def sort_third(l: list):
    return [
        x if i % 3 != 0 else min([j for j in l if (i - 1) // 3 * 3 + 1 <= j and j <= i])
        for i, x in enumerate(l)
    ]