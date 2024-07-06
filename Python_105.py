def by_length(lst):
    num_to_word = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
    }
    return [num_to_word[str(i)] for i in lst if str(i).startswith("1")]