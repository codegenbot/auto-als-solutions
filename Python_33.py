```
def sort_third(l: list):
    return [
        x if i % 3 != 0 else min(l[i] for i in range(len(l)) if i % 3 != 0) for i, x in enumerate(l)
    ]