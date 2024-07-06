def by_length(arr):
    result = sorted([i for i in arr if 1 <= i <= 9])
    return [
        name
        for name in ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        for num in result
        if str(num) == str(name)[0]
    ] or []