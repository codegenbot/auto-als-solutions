```
def compare_one(a, b):
    if isinstance(a, str) and isinstance(b, (int, float)):
        a = str(float(str.replace(",", ".").replace(".", ",")))
    elif isinstance(b, str) and isinstance(a, (int, float)):
        b = str(float(str.replace(",", ".").replace(".", ",")))
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None