```
def sort_third(l: list):
    return [str(i)[-1] if isinstance(i, int) and i % 3 == 0 else str(i) for i in l]