number_names = {
    i: name
    for i, name in [
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
        (4, "Four"),
        (5, "Five"),
        (6, "Six"),
        (7, "Seven"),
        (8, "Eight"),
        (9, "Nine"),
        (10, "Ten"),
    ]
}


def by_length(arr):
    return [number_names[num] for num in arr]