```
def by_length(arr):
    length_mapping = {1: 1, 2: 2, 3: 3, 4: 4, 5: 3, 6: 4, 7: 5, 8: 3, 9: 4}
    word_mapping = {i: word for i, word in zip(length_mapping.values(), ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"])}
    return [word_mapping[i] if i in length_mapping else "" for i in arr]