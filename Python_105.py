def by_length(arr):
    return [name for num, name in zip(sorted(map(str, arr)), ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]) if set(name[0]) == set(str(num)[0])]