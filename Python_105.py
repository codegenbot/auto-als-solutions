def by_length(arr):
    return [names[int(str(i).__len__()) - 1] for i in sorted(arr)]