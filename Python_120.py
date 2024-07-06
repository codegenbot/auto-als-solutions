def maximum(arr, k):
    return sorted([x for x in set(arr)], reverse=True)[:k]