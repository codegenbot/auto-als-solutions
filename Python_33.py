```
def sort_third(l: list):
    return [
        i if i % 3 != 0 else sorted([x for x in l if x % 3 == 0])[min(i % 3, len([x for x in l if x % 3 == 0]) - 1)]
        for i in range(len(l))
    ]