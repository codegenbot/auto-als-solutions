def sort_third(l: list):
    return sorted([x for i, x in enumerate(sorted(l)) if i % 3 == 0])