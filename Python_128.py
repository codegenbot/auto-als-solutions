```
def prod_signs(arr):
    if len(arr) == 0:
        return None
    signs = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
    product = 1
    magnitude_sum = sum(abs(x) for x in arr)
    for sign in signs:
        product *= sign
    return product * magnitude_sum