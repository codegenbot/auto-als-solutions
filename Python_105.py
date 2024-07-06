def by_length(arr):
    result = sorted([i for i in arr if 1 <= i <= 9])
    return [
        name
        for num in result
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
        if str(num) == str(name[:1]).lower()
    ]