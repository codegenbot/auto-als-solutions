def by_length(arr):
    mapping = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
               6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    return [mapping[i] if i in mapping else str(i) for i in arr]