def by_length(arr):
    word_lengths = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
                    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    return [word_lengths[i] for i in arr]