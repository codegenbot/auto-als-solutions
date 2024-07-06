def by_length(arr):
    return [name for num, name in zip(map(str, arr), ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]) if name[0] == '1']