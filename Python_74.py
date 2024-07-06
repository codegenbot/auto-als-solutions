````
def total_match(lst1, lst2):
    sum1 = sum(len(s) for s in lst1)
    sum2 = sum(len(s) for s in lst2)
    if sum1 < sum2:
        return lst1
    elif sum1 > sum2:
        return lst2
    else:
        min_len = min(len(s) for s in lst1 + lst2)
        return [s for s in (lst1 + lst2) if len(s) == min_len]
```