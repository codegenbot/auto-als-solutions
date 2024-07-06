```
def compare_one(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a if float(a.replace(',', '.')) > float(b.replace(',', '.')) else b
    elif isinstance(a, (int, float)):
        return b if isinstance(b, (int, float)) and b > a else None
    elif isinstance(b, (int, float)):
        return a if a > b else None
    else:
        raise ValueError("Invalid input type")