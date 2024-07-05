def sort_third(l: list):
    return [i[-1] if isinstance(i, list) else i for i in l]