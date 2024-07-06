def sort_third(l: list):
    return sorted([x for i, x in enumerate(l) if (i + 1) % 3 == 0], key=lambda y: min([z for z in l if (z - y) % 3 != 0]))