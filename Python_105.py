def by_length(arr):
    result = sorted([i for i in arr if 1 <= i <= 9])
    return [str(num) + " " + ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][num-1] for num in result]