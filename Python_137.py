def compare_one(a, b):
    if isinstance(a, str):
        a = float("".join([i for i in a.replace(",", "")]))
    if isinstance(b, str):
        b = float("".join([i for i in b.replace(",", "")]))
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None