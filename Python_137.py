```
def compare_one(a, b):
    if type(a) == str:
        a = float(''.join(c for c in a.replace(',', '')))
    if type(b) == str:
        b = float(''.join(c for c in b.replace(',', '')))
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None