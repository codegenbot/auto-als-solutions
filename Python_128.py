```
def prod_signs(arr):
    if len(arr) == 0:
        return None
    signs = 1
    for num in arr:
        if num < 0:
            signs *= -1
        elif num > 0:
            signs *= 1
    return sum(abs(num) for num in arr) * signs