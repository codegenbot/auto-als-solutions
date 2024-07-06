def by_length(arr):
    mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9}
    return [name for num, name in zip(map(str, arr), map(str, arr)) if str(num)[0] == "1"]