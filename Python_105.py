def by_length(arr):
    return [
        name
        for num, name in zip(map(str, arr), {str(i): i for i in range(1, 10)})
        if set(name[0]) == {"1"}
    ]