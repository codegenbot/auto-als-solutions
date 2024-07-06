def by_length(arr):
    mapping = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", 
               "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
    return [mapping[str(num)] for num in arr if str(num)[0] == "1"]