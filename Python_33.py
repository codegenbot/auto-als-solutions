def sort_third(l: list):
    return [i if isinstance(i, int) else i[-1] for i in l]