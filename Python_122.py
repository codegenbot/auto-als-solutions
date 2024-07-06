def add_elements(arr, k):
    return sum(i for i in arr[:k] if str(i)[0] == '1')