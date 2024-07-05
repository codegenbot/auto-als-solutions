def sort_third(l: list):
    return [i[-1] if i % 3 == 0 else i for i in l]