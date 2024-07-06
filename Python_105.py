```Python
def by_length(arr):
    result = sorted([i for i in arr if 1 <= i <= 9])
    return [
        name
        for name in [
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        if str(result[0]) == str(name)[0]
    ][:len(result)] or []