```
def get_name(x):
    mapping = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
    return mapping[str(x)]

def by_length(arr):
    return [get_name(x) for x in arr if set(str(x))[0] == "1"]