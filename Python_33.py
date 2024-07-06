def sort_third(l: list):
    return [
        l[i] if i % 3 != 0 else min([x for x in l[i+1:] if (i - x) % 3 != 0], default=l[i])
        for i in range(len(l))
    ]