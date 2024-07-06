```
def unique_digits(x):
    return sorted([int(i) for i in str(x) if len(str(i)) == 1 and int(i) % 2 != 0])