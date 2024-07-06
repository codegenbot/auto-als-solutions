def sort_third(l: list):
    return [
        x if i % 3 != 0 else sorted([y for y in l if (i - 1) // 3 * 3 + j % 3 == i])[j]
        for i in range(len(l))
        for j in range(3)
    ]