def by_length(arr):
    result = sorted([i for i in arr if 1 <= i <= 9])
    return [
        name
        for num, name in zip(
            [str(i) for i in arr],
            ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"],
        )
        if set(name[0]) == set(str(num)[0])
    ]