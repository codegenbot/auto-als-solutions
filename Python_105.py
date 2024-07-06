```
def by_length(arr):
    return [str(num) + " - " + ("One" if num in range(1, 11) else "Unknown") for num in arr]