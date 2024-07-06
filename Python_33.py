```
def sort_third(l):
    result = []
    for i, x in enumerate(l):
        if i % 3 == 0:
            result.append(sorted([y for y in l if i // 3 * 3 <= y < (i + 1) // 3 * 3])[0])
        else:
            result.append(x)
    return result