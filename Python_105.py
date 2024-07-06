def by_length(arr):
    name_number = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
                   6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    return [name_number[i] for i in arr if str(i).startswith('1')]