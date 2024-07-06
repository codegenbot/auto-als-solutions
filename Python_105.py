def by_length(arr):
    words = {
        1: "One",
        2: "To",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    return [words[i] for i in arr if len(words.get(i, "")) >= 4]