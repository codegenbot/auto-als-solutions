```
def by_length(arr):
    result = sorted([str(i) for i in arr])
    return [
        word
        for word in ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        if word[0].lower() == str(num)[0].lower()
    ]