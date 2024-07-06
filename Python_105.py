```Python
def by_length(arr):
    num_to_name = {1: "One", 2: "Two", 3: "Three", 4: "Four", 
                   5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    return [num_to_name[i] for i in arr if len(num_to_name[str(i)]) >= 4]